document.addEventListener('DOMContentLoaded', function() {
    const generateQuizBtn = document.getElementById('generate-quiz-btn');
    const quizContainer = document.getElementById('quiz-container');
    const loadingSpinner = document.getElementById('loading-spinner');

    if (generateQuizBtn) {
        generateQuizBtn.addEventListener('click', function() {
            const noteId = this.dataset.noteId;
            
            // Butonu gizle ve yükleme animasyonunu göster
            generateQuizBtn.style.display = 'none';
            loadingSpinner.classList.remove('hidden');
            quizContainer.innerHTML = ''; // Eski quizi temizle

            fetch(`/note/${noteId}/generate_quiz`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                loadingSpinner.classList.add('hidden');
                if (data.error) {
                    quizContainer.innerHTML = `<p class="error">${data.error}</p>`;
                    generateQuizBtn.style.display = 'block'; // Hata olursa butonu geri getir
                } else {
                    displayQuiz(data.quiz);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                loadingSpinner.classList.add('hidden');
                quizContainer.innerHTML = `<p class="error">Quiz oluşturulurken bir ağ hatası oluştu.</p>`;
                generateQuizBtn.style.display = 'block';
            });
        });
    }
});

function displayQuiz(quiz) {
    const quizContainer = document.getElementById('quiz-container');
    quizContainer.classList.remove('hidden');
    
    let quizHTML = '<h3>Oluşturulan Quiz</h3>';
    quiz.forEach((q, index) => {
        quizHTML += `<div class="quiz-question">`;
        quizHTML += `<p><b>${index + 1}. ${q.question}</b></p>`;
        quizHTML += `<ul class="quiz-options">`;
        q.options.forEach(option => {
            quizHTML += `<li>${option}</li>`;
        });
        quizHTML += `</ul>`;
        quizHTML += `<p class="correct-answer"><i>Doğru Cevap: ${q.correct_answer}</i></p>`;
        quizHTML += `</div>`;
    });

    quizContainer.innerHTML = quizHTML;
}