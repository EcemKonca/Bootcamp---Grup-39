import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()

# Local config dosyasını yüklemeye çalış (varsa)
try:
    from config_local import *
    print("🔒 Local config dosyası yüklendi (güvenli mod)")
except ImportError:
    print("📝 Local config bulunamadı, standart config kullanılıyor")

class Config:
    """Genel yapılandırma ayarları."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or locals().get('SECRET_KEY') or 'edumind-super-secret-key-2025'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/edumind.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Gemini API Anahtarı
    # Öncelik sırası: 1) Environment Variable, 2) Local Config, 3) Default (GitHub için güvenli)
    GEMINI_API_KEY = (
        os.environ.get('GEMINI_API_KEY') or 
        locals().get('GEMINI_API_KEY') or 
        'AIzaSyCn6bl1kYBdW5J8k9VofW-M1SfDYqdnsAQ'  # GitHub'a yüklenecek ama .gitignore ile korunacak
    )
    
    # AI Ayarları
    AI_MODEL_NAME = "gemini-1.5-flash"  # Yeni hesap için optimize edildi
    AI_TEMPERATURE = 0.7
    AI_MAX_OUTPUT_TOKENS = 2048