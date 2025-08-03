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
- **Flask**: Modern Python web framework
- **SQLAlchemy**: ORM ve veritabanı yönetimi
- **SQLite**: Hafif veritabanı çözümü
- **Google Gemini AI**: Yapay zeka analizi
- **JWT**: Güvenli kimlik doğrulama
- **Pydantic**: Veri validasyonu

### Frontend
- **Jinja2 Templates**: Server-side rendering
- **Bootstrap CSS**: Responsive tasarım
- **JavaScript**: İnteraktif özellikler
- **Modern CSS**: Gradient tasarımlar ve animasyonlar

## 🔧 Kurulum

### 1. Projeyi İndirin
```bash
git clone https://github.com/username/EduMind.git
cd EduMind
```

### 2. Python Paketlerini Yükleyin
```bash
pip install -r requirements.txt
```

### 3. API Anahtarı Ayarlayın

#### **🔑 Gemini API Anahtarı Alın:**
1. [Google AI Studio](https://makersuite.google.com/app/apikey)'ya gidin
2. Ücretsiz API anahtarını oluşturun
3. Anahtarı kopyalayın

#### **🔒 Güvenli Kurulum (Önerilen):**

**Seçenek A: Environment Variable (Üretim için)**
```bash
export GEMINI_API_KEY="your_api_key_here"
```

**Seçenek B: config_local.py (Geliştirme için)**
```python
# config_local.py dosyası oluşturun
GEMINI_API_KEY = 'your_api_key_here'
```

### 4. Uygulamayı Başlatın
```bash
python run.py
```

### 5. Tarayıcıda Açın
```
http://localhost:5000
```

## 🔒 GitHub Güvenliği

Bu proje API anahtarlarını güvenli şekilde yönetir:

- ✅ `.gitignore` dosyası hassas bilgileri korur
- ✅ `config_local.py` yerel geliştirme için kullanılır
- ✅ Environment variable desteği vardır
- ✅ API anahtarları GitHub'a yüklenmez

**⚠️ Önemli:** `config_local.py` dosyanızı asla GitHub'a yüklemeyin!

## 🎯 Kullanım

### **📝 Not Oluşturma:**
1. "Yeni Not" butonuna tıklayın
2. Başlık ve içerik girin
3. AI otomatik olarak özet ve anahtar kelimeler oluşturur

### **🧠 AI Analizi:**
1. Dashboard'dan bir nota "🧠 Analiz" tıklayın
2. Detaylı AI analizini görün
3. "Quiz Oluştur" ile test soruları üretin

### **🎮 Demo Modu:**
- API anahtarı olmadan da çalışır
- Örnek özetler ve analizler gösterir
- Gerçek AI için API anahtarı gereklidir

## 📊 Demo vs Gerçek AI

| Özellik | Demo Modu | Gerçek AI |
|---------|-----------|-----------|
| Özetleme | ✅ Örnek cevaplar | ✅ Gerçek analiz |
| Anahtar Kelimeler | ✅ Sabit kelimeler | ✅ Dinamik çıkarım |
| Quiz Oluşturma | ✅ Örnek sorular | ✅ İçerik bazlı sorular |
| Yaş Grubu Uyarlaması | ❌ | ✅ |
| Maliyet | 🆓 Ücretsiz | 🆓 Ücretsiz (limitle) |

# 🌀 Sprint 1

---

## 📝 Sprint Notları  
User Story'ler, product backlog içerisine yazılmıştır.  
Her bir backlog item'ına tıklandığında ilgili kullanıcı hikayesinin detayı okunabilir durumdadır.  
Projenin temel işlevleri belirlendi ve görevler kategorilere ayrılarak planlandı.

---

## 🎯 Sprint İçinde Tamamlanması Tahmin Edilen Puan  
**100 Puan**

---

## 📐 Puan Tamamlama Mantığı  
Proje genelinde 300 puanlık bir backlog belirlenmiştir.Bu görevler 3 sprint'e bölünmüş ve ilk sprintte 100 puanlık iş yapılması hedeflenmiştir. İlk sprint, proje fikrinin netleştirilmesi ve temel planlama aşamalarını kapsayacak şekilde düzenlenmiştir.

---

## ☕ Daily Scrum  
Daily Scrum toplantılarının **WhatsApp grubu** üzerinden yapılmasına karar verilmiştir.

---

## 📌 Sprint Board Güncellemesi  
Sprint süresince görev takibi **Trello** üzerinden yapılmıştır.  
🖼️ ![image](https://github.com/user-attachments/assets/39bb0f45-76d6-4c7a-9f02-66b3a9850bac)


---

## 🖥️ Ürün Durumu (Sprint 1)

- Proje fikri belirlendi: **EduMind – AI Destekli Kişiselleştirilmiş Öğrenme Koçu**
- Hedef kullanıcı kitlesi ve çözülmek istenen problem netleştirildi  
- Kullanıcı senaryoları ve temel fonksiyon listesi hazırlandı  
- Kullanılacak teknolojiler belirlendi: **Python, Flask, Gemini API**  
- Product backlog oluşturularak story point'ler atandı  
- Ekip içi görev dağılımı ve roadmap planlaması tamamlandı  

---

## 🗣️ Sprint Review  

Ekip üyeleri, proje fikri ve görev dağılımları hakkında fikirlerini sundu.  
Proje yönünün hem teknik olarak uygulanabilir hem de faydalı bulunduğu konusunda uzlaşıldı.  
Kullanıcı senaryoları ve temel işlevlerin net oluşu, sonraki sprintlere sağlam bir temel oluşturdu.

**Sprint Review Katılımcıları:**  
- Ecem  
- İsra  

---

## 🔍 Sprint Retrospective  

### ✅ Güçlü Yönler:
- Ekip içinde fikir alışverişi güçlüydü, kararlar oy birliğiyle alındı  
- Görevler kişilere net şekilde dağıtıldı  
- Kullanıcı senaryoları detaylıca düşünüldü  

### ⚠️ İyileştirilmesi Gereken Noktalar:
- İletişimin daha da hızlanması için Daily Scrum zamanlarının sabitlenmesine karar verildi  
- Teknik araştırmalara daha erken başlanması gerektiği fark edildi  


## 🌀 Sprint 2

---

### 📝 Sprint Notları  
Bu sprintte projenin temel yazılım altyapısı oluşturuldu.  
Backend tarafında Flask ile API yapısı kuruldu, kullanıcı kimlik doğrulama ve not yönetimi sistemleri geliştirildi.  
Frontend tarafında ise modern responsive tasarım ile kullanıcı arayüzü geliştirildi.  
Tasarım, veri akışı ve kullanıcı etkileşimi temel alınarak component yapısı oturtuldu.  

---

### 🎯 Sprint İçinde Tamamlanması Tahmin Edilen Puan  
**100 Puan**

---

### 📐 Puan Tamamlama Mantığı  
Toplam 300 puanlık backlog'un ikinci sprintinde, ürünün teknik altyapısının kodlandığı 100 puanlık işler yapılmıştır.

---

### ☕ Daily Scrum  
- Daily Scrum toplantıları Discord üzerinden yapılmaya devam etti.  
- Ayrıca günlük ilerleme durumu WhatsApp grubundan paylaşıldı.

---

### 📌 Sprint Board Güncellemesi  
- Görev takibi Trello üzerinden sürdürüldü.  
🖼️ <img width="1425" height="747" alt="image" src="https://github.com/user-attachments/assets/52b1f84f-a065-4786-94c8-324cea4e30f4" />


---

### 🖥️ Ürün Durumu (Sprint 2)

#### ✅ Backend Geliştirmeleri
- Flask ile temel proje yapısı kuruldu  
- Kullanıcı kayıt ve giriş sistemi geliştirildi (Flask-Login Authentication)  
- Not ve quiz işlemleri için CRUD endpoint'leri yazıldı  
- Veritabanı bağlantısı kuruldu ve modeller oluşturuldu  
- `requirements.txt` ile bağımlılıklar listelendi  

#### ✅ Frontend Geliştirmeleri
- Giriş/kayıt sayfaları tasarlandı  
- Form bileşenleri geliştirildi  
- Flask-Login ile oturum yönetimi kuruldu  
- Modern CSS tasarımı ve responsive layout eklendi  

#### ✅ AI Entegrasyonu
- Google Gemini API entegrasyonu tamamlandı
- Akıllı özetleme ve anahtar kelime çıkarma
- Quiz oluşturma özellikleri
- Demo modu ile güvenli geliştirme

---

### 🗣️ Sprint Review  

- Projenin teknik altyapısı tamamlandı ve fonksiyonel hale getirildi  
- Frontend ve backend taraflarının entegre çalışması sağlandı  
- Kod yapısı modüler, anlaşılır ve sürdürülebilir olarak inşa edildi  
- AI entegrasyonu başarıyla gerçekleştirildi

**Katılımcılar:**  
- Ecem  
- Furkan  
- İsra  

---

### 🔍 Sprint Retrospective  

#### ✅ Güçlü Yönler:
- Backend ve frontend çalışmaları eşzamanlı ve dengeli ilerledi  
- Kod yapısı açık, düzenli ve geliştirilebilir şekilde yazıldı  
- İletişim kesintisiz sürdürüldü, görev dağılımı net yapıldı  
- AI entegrasyonu beklenenden daha başarılı oldu

#### ⚠️ İyileştirme Alanları:
- API güvenliği ve .gitignore yapılandırması tamamlandı  
- Frontend tarafında daha fazla interaktivite eklenebilir  
- Unit test altyapısı bir sonraki sprintte planlanacak  

---

## 🌀 Sprint 3

---

### 📝 Sprint Notları  
Bu sprintte EduMind platformunun kullanıcı deneyimi geliştirildi, AI özellikleri güçlendirildi ve sistem üretim öncesi güvenlik–performans optimizasyonlarından geçirildi.  
Not yönetimine klasörleme, gelişmiş arama ve istatistik grafikleri eklendi.  
AI tarafında metin analizi ve quiz oluşturma özellikleri devreye alındı.  

---

### 🎯 Sprint İçinde Tamamlanması Tahmin Edilen Puan  
**100 Puan**

---

### 📐 Puan Tamamlama Mantığı  
Toplam 300 puanlık backlog’un üçüncü ve son sprintinde, kullanıcı deneyimi ve AI yeteneklerini geliştiren 100 puanlık işler tamamlandı.  
Bu sprint, projenin üretim öncesi son hazırlıklarını kapsadı.  

---

### ☕ Daily Scrum  
- Daily Scrum toplantıları Discord üzerinden gerçekleştirildi.  
- Günlük ilerleme raporları ve hata bildirimleri WhatsApp grubundan paylaşıldı.  

---

### 📌 Sprint Board Güncellemesi  
- Görev takibi Trello üzerinden sürdürüldü.  
<img width="1430" height="691" alt="image" src="https://github.com/user-attachments/assets/3c07e836-a93a-4125-b012-b7f3a5ab1ab2" />


---

### 🖥️ Ürün Durumu (Sprint 3)

#### ✅ Yeni Özellikler
- **Gelişmiş AI Analizi**  
  - Metin anahtar kelime tespiti  
  - Not analizi
  - Not içeriğine göre quiz oluşturma
- **Not Yönetimi İyileştirmeleri**  
  - Notu basit veya detaylı açıklama seçeneği
  - Detaylı not istatistiği


#### ✅ İyileştirmeler
- SQLAlchemy ile veritabanı sorgu optimizasyonu  
- AI çağrılarında cache mekanizması ile hız optimizasyonu  

#### ✅ Güvenlik ve Test
- XSS ve CSRF korumaları  
- Kullanıcı dostu API hata mesajları  
- Birim testler ile API ve veritabanı işlemleri doğrulandı  

---

### 🗣️ Sprint Review  
- Kullanıcı deneyimi açısından platform daha zengin hale getirildi  
- AI analizleri kişiselleştirilmiş ve içerik odaklı şekilde geliştirildi  
- Not analizi ve metin içeriğine göre quiz oluşturma eklendi 
- Öğrenme sürecini görselleştiren dinamik grafikler başarıyla entegre edildi  
- Güvenlik ve performans optimizasyonları tamamlanarak üretime hazır hale getirildi  

**Katılımcılar:**  
- Ecem  
- Furkan  
- İsra  

---

### 🔍 Sprint Retrospective  

#### ✅ Güçlü Yönler:
- Kullanıcı odaklı geliştirmeler başarıyla tamamlandı  
- AI özellikleri içerik zenginliği açısından ileri seviyeye taşındı  
- Takım içi iletişim sprint boyunca hızlı ve netti  
- Test ve güvenlik adımları eksiksiz tamamlandı  

#### ⚠️ İyileştirme Alanları:
- Bir sonraki projede test otomasyon kapsamı genişletilebilir  
- Mobil cihazlarda performans ölçümleri daha erken yapılabilir  
- Kullanıcı geri bildirimleri daha sık toplanarak geliştirme sürecine entegre edilebilir  



## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

## 🌟 Teşekkürler

- Google Gemini AI ekibine
- Flask toplulukuna
- Tüm açık kaynak katkıda bulunanlar

