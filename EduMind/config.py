import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()

class Config:
    """Genel yapılandırma ayarları."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'varsayilan-gizli-anahtar'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/edumind.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')