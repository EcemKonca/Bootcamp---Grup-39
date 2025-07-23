from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login' # Login olmayan kullanıcıyı yönlendir
login_manager.login_message_category = 'info'

def create_app():
    """Uygulama ve eklentileri başlatan factory fonksiyonu."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Instance folder'ın var olduğundan emin ol
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    with app.app_context():
        db.create_all() # Veritabanı tablolarını oluştur

    return app