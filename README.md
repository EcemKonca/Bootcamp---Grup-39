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

# 🌀 Sprint 1

---

## 📝 Sprint Notları  
User Story’ler, product backlog içerisine yazılmıştır.  
Her bir backlog item’ına tıklandığında ilgili kullanıcı hikayesinin detayı okunabilir durumdadır.  
Projenin temel işlevleri belirlendi ve görevler kategorilere ayrılarak planlandı.

---

## 🎯 Sprint İçinde Tamamlanması Tahmin Edilen Puan  
**100 Puan**

---

## 📐 Puan Tamamlama Mantığı  
Proje genelinde 300 puanlık bir backlog belirlenmiştir.Bu görevler 3 sprint’e bölünmüş ve ilk sprintte 100 puanlık iş yapılması hedeflenmiştir. İlk sprint, proje fikrinin netleştirilmesi ve temel planlama aşamalarını kapsayacak şekilde düzenlenmiştir.

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
- Kullanılacak teknolojiler belirlendi: **Python, FastAPI, Gemini API**  
- Product backlog oluşturularak story point’ler atandı  
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
Backend tarafında FastAPI ile API yapısı kuruldu, kullanıcı kimlik doğrulama ve not yönetimi sistemleri geliştirildi.  
Frontend tarafında ise React ile kullanıcı arayüzü iskeleti kuruldu.  
Tasarım, veri akışı ve kullanıcı etkileşimi temel alınarak component yapısı oturtuldu.  

---

### 🎯 Sprint İçinde Tamamlanması Tahmin Edilen Puan  
**100 Puan**

---

### 📐 Puan Tamamlama Mantığı  
Toplam 300 puanlık backlog’un ikinci sprintinde, ürünün teknik altyapısının kodlandığı 100 puanlık işler yapılmıştır.

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
- FastAPI ile temel proje yapısı kuruldu  
- Kullanıcı kayıt ve giriş sistemi geliştirildi (JWT Authentication)  
- Not ve quiz işlemleri için CRUD endpoint’leri yazıldı  
- Veritabanı bağlantısı kuruldu ve modeller oluşturuldu  
- `requirements.txt` ile bağımlılıklar listelendi  

#### ✅ Frontend Geliştirmeleri
- Giriş/kayıt sayfaları tasarlandı  
- Form bileşenleri geliştirildi  
- Auth context ile oturum yönetimi kuruldu  
- Backend ile ilk API entegrasyonu başarıyla yapıldı  

---

### 🗣️ Sprint Review  

- Projenin teknik altyapısı tamamlandı ve fonksiyonel hale getirildi  
- Frontend ve backend taraflarının entegre çalışması sağlandı  
- Kod yapısı modüler, anlaşılır ve sürdürülebilir olarak inşa edildi  

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

#### ⚠️ İyileştirme Alanları:
- API dökümantasyonu eksik → Sprint 3’te Swagger entegrasyonu planlandı  
- Frontend tarafında test altyapısı kurulmamış → Jest/React Testing Library araştırılacak  
- Commit mesajlarının daha açıklayıcı olması gerekiyor → Commit format rehberi hazırlanacak  

---


