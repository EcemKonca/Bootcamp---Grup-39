document.addEventListener('DOMContentLoaded', function() {
    const generateQuizBtn = document.getElementById('generate-quiz-btn');
    const quizContainer = document.getElementById('quiz-container');
    const loadingSpinner = document.getElementById('loading-spinner');

    if (generateQuizBtn) {
        generateQuizBtn.addEventListener('click', function() {
            const noteId = this.dataset.noteId;
            console.log('Quiz butonu tıklandı, note ID:', noteId);
            
            // Butonu gizle ve yükleme animasyonunu göster
            generateQuizBtn.style.display = 'none';
            loadingSpinner.classList.remove('hidden');
            quizContainer.innerHTML = ''; // Eski quizi temizle
            quizContainer.classList.add('hidden'); // Quiz container'ı gizle

            console.log('Quiz API request başlatılıyor...');

            fetch(`/note/${noteId}/generate_quiz`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    difficulty: 'medium'
                })
            })
            .then(response => {
                console.log('Response alındı:', response.status, response.statusText);
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Quiz data alındı:', data);
                loadingSpinner.classList.add('hidden');
                generateQuizBtn.style.display = 'block'; // Butonu geri getir
                
                if (data.error) {
                    console.error('Backend hatası:', data.error);
                    quizContainer.innerHTML = `<div class="error">❌ Hata: ${data.error}</div>`;
                    quizContainer.classList.remove('hidden');
                } else if (data.quiz && Array.isArray(data.quiz)) {
                    console.log('Quiz gösteriliyor, soru sayısı:', data.quiz.length);
                    displayQuiz(data.quiz, data.mode || 'unknown');
                } else {
                    console.error('Geçersiz quiz formatı:', data);
                    quizContainer.innerHTML = `<div class="error">❌ Quiz formatı geçersiz</div>`;
                    quizContainer.classList.remove('hidden');
                }
            })
            .catch(error => {
                console.error('Quiz oluşturma hatası:', error);
                loadingSpinner.classList.add('hidden');
                generateQuizBtn.style.display = 'block';
                
                let errorMessage = 'Bilinmeyen hata oluştu';
                if (error.message.includes('Failed to fetch')) {
                    errorMessage = 'Sunucuya bağlanılamadı. Lütfen tekrar deneyin.';
                } else if (error.message.includes('HTTP 500')) {
                    errorMessage = 'Sunucu hatası oluştu. Lütfen daha sonra tekrar deneyin.';
                } else if (error.message.includes('HTTP 403')) {
                    errorMessage = 'Bu işlem için yetkiniz bulunmuyor.';
                } else {
                    errorMessage = error.message;
                }
                
                quizContainer.innerHTML = `<div class="error">❌ Quiz oluşturulurken hata: ${errorMessage}</div>`;
                quizContainer.classList.remove('hidden');
            });
        });
    }
});

function displayQuiz(quiz, mode = 'unknown') {
    const quizContainer = document.getElementById('quiz-container');
    quizContainer.classList.remove('hidden');
    
    let quizHTML = '<div class="quiz-header">';
    quizHTML += '<h3>🎮 Oluşturulan Quiz</h3>';
    
    // Mode badge ekle
    if (mode === 'demo') {
        quizHTML += '<span class="mode-badge demo">📝 Demo Modu</span>';
    } else if (mode === 'ai') {
        quizHTML += '<span class="mode-badge ai">🤖 AI Destekli</span>';
    }
    
    quizHTML += '</div>';
    
    if (!quiz || quiz.length === 0) {
        quizHTML += '<div class="error">❌ Quiz soruları bulunamadı</div>';
    } else {
        quiz.forEach((q, index) => {
            quizHTML += `<div class="quiz-question">`;
            quizHTML += `<h4>${index + 1}. ${q.question}</h4>`;
            
            if (q.options && Array.isArray(q.options)) {
                quizHTML += `<ul class="quiz-options">`;
                q.options.forEach((option, optIndex) => {
                    const letter = String.fromCharCode(65 + optIndex); // A, B, C, D
                    quizHTML += `<li><strong>${letter})</strong> ${option}</li>`;
                });
                quizHTML += `</ul>`;
            }
            
            if (q.correct_answer) {
                quizHTML += `<div class="correct-answer">✅ <strong>Doğru Cevap:</strong> ${q.correct_answer}</div>`;
            }
            
            if (q.explanation) {
                quizHTML += `<div class="explanation">💡 <strong>Açıklama:</strong> ${q.explanation}</div>`;
            }
            
            quizHTML += `</div>`;
        });
        
        // Quiz bitişi
        quizHTML += '<div class="quiz-footer">';
        quizHTML += `<p><strong>🎯 Toplam ${quiz.length} soru oluşturuldu!</strong></p>`;
        quizHTML += '<button onclick="window.print()" class="btn btn-outline">🖨️ Yazdır</button>';
        quizHTML += '</div>';
    }

    quizContainer.innerHTML = quizHTML;
    
    // Quiz container'a scroll yap
    quizContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Akıllı Açıklayıcı (ELI5/15) özelliği
document.addEventListener('DOMContentLoaded', function() {
    const noteContentContainer = document.querySelector('.content-text'); // Hedefimiz notun içeriği
    const selectionMenu = document.getElementById('text-selection-menu');
    const modal = document.getElementById('explanation-modal');
    const closeModalBtn = document.querySelector('.modal-close-btn');
    const explanationResultDiv = document.getElementById('explanation-result');
    let selectedText = '';

    if (noteContentContainer) {
        // Metin seçimi bittiğinde menüyü göster
        noteContentContainer.addEventListener('mouseup', function(e) {
            selectedText = window.getSelection().toString().trim();
            if (selectedText.length > 3 && selectedText.length < 300) { // Çok kısa veya çok uzun metinleri engelle
                selectionMenu.style.left = `${e.pageX - 50}px`;
                selectionMenu.style.top = `${e.pageY + 15}px`;
                selectionMenu.style.display = 'flex';
            } else {
                selectionMenu.style.display = 'none';
            }
        });
    }

    // Sayfaya tıklayınca menüyü gizle (menünün kendisi hariç)
    document.addEventListener('mousedown', function(e) {
        if (selectionMenu && !selectionMenu.contains(e.target)) {
            selectionMenu.style.display = 'none';
        }
    });

    // Menüdeki butonlara tıklandığında
    if (selectionMenu) {
        selectionMenu.addEventListener('click', function(e) {
            if (e.target.classList.contains('menu-btn')) {
                const complexity = e.target.dataset.complexity;
                getExplanation(complexity);
            }
        });
    }

    // Açıklama isteme fonksiyonu
    function getExplanation(complexity) {
        if (selectedText) {
            selectionMenu.style.display = 'none';
            explanationResultDiv.innerHTML = '<p>🤖 AI düşünüyor...</p>';
            modal.style.display = 'flex';

            fetch('/explain-text', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: selectedText, complexity: complexity })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    explanationResultDiv.innerHTML = `<p style="color: red;">Hata: ${data.error}</p>`;
                } else {
                    explanationResultDiv.innerHTML = data.explanation;
                }
            })
            .catch(error => {
                console.error('Fetch Error:', error);
                explanationResultDiv.innerHTML = '<p style="color: red;">Bir ağ hatası oluştu.</p>';
            });
        }
    }

    // Modal pencereyi kapatma
    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', () => modal.style.display = 'none');
    }
    window.addEventListener('click', (e) => {
        if (e.target == modal) {
            modal.style.display = 'none';
        }
    });
});