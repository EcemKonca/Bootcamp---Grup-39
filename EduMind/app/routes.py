from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from app import db
from app.forms import RegistrationForm, LoginForm, NoteForm
from app.models import User, Note
from flask_login import login_user, current_user, logout_user, login_required
from app.ai_services import summarize_and_get_keywords, generate_quiz_from_text

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
@main_bp.route("/home")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

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
        
        # --- YAPAY ZEKA ENTEGRASYONU (ÖZETLEME) ---
        ai_result = summarize_and_get_keywords(form.content.data)
        note.summary = ai_result.get('summary', 'Özet alınamadı.')
        note.keywords = ai_result.get('keywords', '')
        # --- BİTİŞ ---

        db.session.add(note)
        db.session.commit()
        flash('Notunuz başarıyla oluşturuldu ve yapay zeka tarafından analiz edildi!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('create_note.html', title='Yeni Not', form=form)

@main_bp.route("/note/<int:note_id>")
@login_required
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    return render_template('view_note.html', title=note.title, note=note)

@main_bp.route("/note/<int:note_id>/generate_quiz", methods=['POST'])
@login_required
def generate_quiz(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        return jsonify({"error": "Yetkisiz işlem"}), 403
    
    # --- YAPAY ZEKA ENTEGRASYONU (QUIZ) ---
    quiz_data = generate_quiz_from_text(note.content)
    # --- BİTİŞ ---

    if "error" in quiz_data:
        return jsonify(quiz_data), 500
        
    return jsonify(quiz_data)