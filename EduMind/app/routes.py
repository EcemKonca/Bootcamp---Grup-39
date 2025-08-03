from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify, abort
from app import db
from app.forms import RegistrationForm, LoginForm, NoteForm
from app.models import User, Note
from flask_login import login_user, current_user, logout_user, login_required
from app.ai_services import enhanced_summarize_and_get_keywords, generate_enhanced_quiz_from_text, summarize_and_get_keywords, generate_quiz_from_text

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
@main_bp.route("/home")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main_bp.route("/quiz-test")
def quiz_test():
    """Quiz debugging için test sayfası"""
    from flask import send_from_directory
    import os
    return send_from_directory(os.getcwd(), 'test_quiz.html')

@main_bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, age_group=form.age_group.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Hesabınız oluşturuldu! Şimdi giriş yapabilirsiniz.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Kayıt Ol', form=form)

@main_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Giriş başarısız. Lütfen e-posta ve şifrenizi kontrol edin.', 'danger')
    return render_template('login.html', title='Giriş Yap', form=form)

@main_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main_bp.route("/dashboard")
@login_required
def dashboard():
    notes = Note.query.filter_by(author=current_user).order_by(Note.date_posted.desc()).all()
    return render_template('dashboard.html', title='Kontrol Paneli', notes=notes)

@main_bp.route("/note/new", methods=['GET', 'POST'])
@login_required
def create_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(title=form.title.data, content=form.content.data, author=current_user)
        
        # --- GELIŞMIŞ YAPAY ZEKA ENTEGRASYONU ---
        # Kullanıcının yaş grubuna göre özetleme
        user_level = current_user.age_group if current_user.age_group else "teen"
        ai_result = enhanced_summarize_and_get_keywords(form.content.data, user_level)
        
        note.summary = ai_result.get('summary', 'Özet alınamadı.')
        note.keywords = ai_result.get('keywords', '')
        # --- BİTİŞ ---

        db.session.add(note)
        db.session.commit()
        
        # AI modu bilgisi ile flash mesajı
        ai_mode = ai_result.get('mode', 'unknown')
        if ai_mode == 'demo':
            flash('Notunuz oluşturuldu! (Demo modu - Gerçek AI için API anahtarı gerekli)', 'info')
        elif ai_mode == 'ai':
            flash('Notunuz başarıyla oluşturuldu ve yapay zeka tarafından analiz edildi! ✨', 'success')
        else:
            flash('Notunuz oluşturuldu ancak AI analizi sırasında sorun yaşandı.', 'warning')
            
        return redirect(url_for('main.dashboard'))
    return render_template('create_note.html', title='Yeni Not', form=form)

@main_bp.route("/note/<int:note_id>")
@login_required
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    return render_template('view_note.html', title=note.title, note=note)

@main_bp.route("/note/<int:note_id>/analyze", methods=['GET', 'POST'])
@login_required
def analyze_note(note_id):
    """Gelişmiş not analizi sayfası"""
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        return redirect(url_for('main.dashboard'))
    
    analysis = None
    if request.method == 'POST':
        # Yeniden analiz et
        user_level = current_user.age_group if current_user.age_group else "teen"
        analysis = enhanced_summarize_and_get_keywords(note.content, user_level)
        
        # Veritabanını güncelle
        note.summary = analysis.get('summary', note.summary)
        note.keywords = analysis.get('keywords', note.keywords)
        db.session.commit()
        
        flash('Not yeniden analiz edildi! 🔄', 'success')
    else:
        # Mevcut analizi göster
        analysis = {
            'summary': note.summary,
            'keywords': note.keywords,
            'word_count': len(note.content.split()) if note.content else 0,
            'mode': 'existing'
        }
    
    return render_template('analyze_note.html', title=f'{note.title} - Analiz', note=note, analysis=analysis)

@main_bp.route("/note/<int:note_id>/generate_quiz", methods=['POST'])
@login_required
def generate_quiz(note_id):
    print(f"🎮 Quiz oluşturma başlatıldı - Note ID: {note_id}")
    
    try:
        note = Note.query.get_or_404(note_id)
        print(f"📝 Not bulundu: {note.title}")
        
        if note.author != current_user:
            print("❌ Yetki hatası: Not başka kullanıcıya ait")
            return jsonify({"error": "Yetkisiz işlem"}), 403
        
        # Zorluk seviyesi parametresi
        difficulty = 'medium'
        if request.is_json and request.json:
            difficulty = request.json.get('difficulty', 'medium')
        print(f"🎯 Zorluk seviyesi: {difficulty}")
        
        # Not içeriği kontrolü
        if not note.content or len(note.content.strip()) < 50:
            print("❌ Not içeriği çok kısa")
            return jsonify({
                "error": "Not içeriği quiz oluşturmak için çok kısa. En az 50 karakter gerekli.",
                "mode": "error"
            }), 400
        
        print(f"📖 Not içeriği uzunluğu: {len(note.content)} karakter")
        
        # --- GELIŞMIŞ YAPAY ZEKA QUIZ ENTEGRASYONU ---
        print("🤖 AI quiz oluşturma başlatılıyor...")
        quiz_data = generate_enhanced_quiz_from_text(note.content, difficulty)
        print(f"✅ AI cevabı alındı: {quiz_data}")
        # --- BİTİŞ ---

        if "error" in quiz_data:
            print(f"❌ AI hatası: {quiz_data['error']}")
            return jsonify(quiz_data), 500
        
        if "quiz" not in quiz_data or not quiz_data["quiz"]:
            print("❌ Quiz verisi boş")
            return jsonify({
                "error": "Quiz oluşturulamadı - boş veri döndü",
                "mode": "error"
            }), 500
            
        print(f"🎯 Başarılı! {len(quiz_data['quiz'])} soru oluşturuldu")
        return jsonify(quiz_data)
        
    except Exception as e:
        print(f"🔴 Quiz route hatası: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "error": f"Sunucu hatası: {str(e)}",
            "mode": "error"
        }), 500

@main_bp.route("/ai-demo")
@login_required
def ai_demo():
    """AI özelliklerini test etmek için demo sayfası"""
    return render_template('ai_demo.html', title='AI Demo')

@main_bp.route("/api/analyze_text", methods=['POST'])
@login_required
def api_analyze_text():
    """AJAX için metin analizi API"""
    if not request.is_json:
        return jsonify({"error": "JSON gerekli"}), 400
    
    text = request.json.get('text', '').strip()
    if not text:
        return jsonify({"error": "Metin boş olamaz"}), 400
    
    user_level = current_user.age_group if current_user.age_group else "teen"
    analysis = enhanced_summarize_and_get_keywords(text, user_level)
    
    return jsonify(analysis)

@main_bp.route("/stats")
@login_required
def stats():
    notes = Note.query.filter_by(author=current_user).all()
    total_notes = len(notes)
    total_words = sum(len(note.content.split()) for note in notes)
    avg_words = total_words / total_notes if total_notes > 0 else 0

    # En çok geçen kelimeler
    from collections import Counter
    words = []
    for note in notes:
        words.extend(note.content.lower().split())
    common_words = Counter(words).most_common(5)

    # AI kullanım istatistikleri
    ai_analyzed_notes = len([note for note in notes if note.summary and "hata" not in note.summary.lower()])
    ai_usage_rate = (ai_analyzed_notes / total_notes * 100) if total_notes > 0 else 0

    return render_template(
        "stats.html",
        title="Not İstatistikleri",
        total_notes=total_notes,
        total_words=total_words,
        avg_words=avg_words,
        common_words=common_words,
        ai_analyzed_notes=ai_analyzed_notes,
        ai_usage_rate=ai_usage_rate
    )

@main_bp.route("/explain-text", methods=['POST'])
@login_required
def explain_text_route():
    data = request.get_json()
    if not data or 'text' not in data or 'complexity' not in data:
        return jsonify({"error": "Eksik bilgi gönderildi."}), 400

    selected_text = data.get('text')
    complexity_level = data.get('complexity')

    from app.ai_services import explain_text
    result = explain_text(selected_text, complexity_level)
    
    return jsonify(result)