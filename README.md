# EduMind - Yapay Zeka Destekli Eğitim Platformu

EduMind, yapay zeka teknolojilerini kullanarak kişiselleştirilmiş öğrenme deneyimi sunan modern bir eğitim platformudur.

## 🚀 Özellikler

- **Akıllı Not Alma**: Yapay zeka destekli not organizasyonu ve özetleme
- **Kişiselleştirilmiş Quizler**: AI ile oluşturulan özel sınavlar
- **Öğrenme Takibi**: Detaylı ilerleme raporları ve istatistikler
- **Modern Arayüz**: Kullanıcı dostu ve responsive tasarım
- **Güvenli Kimlik Doğrulama**: JWT tabanlı güvenli giriş sistemi

## 🛠️ Teknolojiler

### Backend
- **FastAPI**: Modern, hızlı Python web framework
- **SQLAlchemy**: ORM ve veritabanı yönetimi
- **SQLite**: Hafif veritabanı çözümü
- **JWT**: Güvenli kimlik doğrulama
- **Pydantic**: Veri validasyonu

### Frontend
- **React**: Modern JavaScript UI kütüphanesi
- **TypeScript**: Type-safe geliştirme
- **Tailwind CSS**: Utility-first CSS framework
- **React Router**: Client-side routing
- **Context API**: State management

## 📦 Kurulum

### Gereksinimler
- Python 3.8+
- Node.js 14+
- npm veya yarn

### Backend Kurulumu

```bash
# Backend dizinine geç
cd backend

# Sanal ortam oluştur
python -m venv venv

# Sanal ortamı aktifleştir
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Uygulamayı başlat
uvicorn app.main:app --reload
```

### Frontend Kurulumu

```bash
# Frontend dizinine geç
cd frontend

# Bağımlılıkları yükle
npm install

# Uygulamayı başlat
npm start
```

## 🎯 Kullanım

1. **Backend**: http://localhost:8000 adresinde çalışır
2. **Frontend**: http://localhost:3000 adresinde çalışır
3. **API Dokümantasyonu**: http://localhost:8000/docs

## 📁 Proje Yapısı

```
EduMind/
├── backend/
│   ├── app/
│   │   ├── models/         # Veritabanı modelleri
│   │   ├── routers/        # API endpoint'leri
│   │   ├── services/       # İş mantığı
│   │   └── database.py     # Veritabanı konfigürasyonu
│   └── requirements.txt    # Python bağımlılıkları
├── frontend/
│   ├── src/
│   │   ├── components/     # React bileşenleri
│   │   ├── pages/         # Sayfa bileşenleri
│   │   ├── context/       # Context API
│   │   └── App.tsx        # Ana uygulama
│   └── package.json       # Node.js bağımlılıkları
└── README.md
```

## 🔧 Geliştirme

### Backend Geliştirme
- FastAPI otomatik reload ile çalışır
- API dokümantasyonu `/docs` endpoint'inde mevcuttur
- Veritabanı değişiklikleri için migration kullanın

### Frontend Geliştirme
- React hot reload aktiftir
- TypeScript strict mode kullanılır
- Tailwind CSS utility classes kullanın

## 🚀 Deployment

### Backend Deployment
```bash
# Production için
pip install gunicorn
gunicorn app.main:app -k uvicorn.workers.UvicornWorker
```

### Frontend Deployment
```bash
# Build oluştur
npm run build

# Build klasörünü static hosting'e yükle
```

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👥 Geliştirici Ekibi

- **Bootcamp Grup 39** - Tam Stack Geliştirme

## 📞 İletişim

Proje hakkında sorularınız için GitHub Issues kullanabilirsiniz.

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

