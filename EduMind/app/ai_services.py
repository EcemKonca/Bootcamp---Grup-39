import google.generativeai as genai
from config import Config
import json
import re

# Demo modu için daha zengin örnek cevaplar
DEMO_RESPONSES_BANK = [
    {
        "summary": "Bu metin, önemli kavramları ve temel bilgileri içermektedir. Ana konular arasında temel prensipler, pratik uygulamalar ve öğrenme hedefleri yer almaktadır. Metinde sunulan bilgiler öğrencilerin konuyu daha iyi anlamasına yardımcı olacak şekilde düzenlenmiştir.",
        "keywords": "öğrenme, kavram, uygulama, prensip, hedef, bilgi, temel"
    },
    {
        "summary": "Bu içerik, konuyla ilgili temel bilgileri sistematik bir şekilde sunmaktadır. Metinde yer alan açıklamalar ve örnekler, öğrencilerin konuyu derinlemesine kavramasını sağlamaktadır. Ana fikirler mantıklı bir sıra ile organize edilmiştir.",
        "keywords": "sistematik, açıklama, örnek, organize, mantıklı, kavrama, derinlemesine"
    },
    {
        "summary": "Sunulan metin, konu hakkında kapsamlı bir bakış açısı sunmaktadır. İçerikte yer alan detaylar ve açıklamalar, öğrencilerin konuyu farklı perspektiflerden değerlendirmesine olanak tanımaktadır. Bilgiler güncel ve uygulanabilir niteliktedir.",
        "keywords": "kapsamlı, bakış açısı, detay, perspektif, güncel, uygulanabilir, değerlendirme"
    }
]

# API anahtarını yapılandır
api_available = False
model = None

try:
    if Config.GEMINI_API_KEY and Config.GEMINI_API_KEY.strip():
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # Gelişmiş model yapılandırması
        generation_config = {
            "temperature": Config.AI_TEMPERATURE,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": Config.AI_MAX_OUTPUT_TOKENS,
        }
        
        # Güvenlik ayarları
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]
        
        model = genai.GenerativeModel(
            model_name=Config.AI_MODEL_NAME,
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        
        # Model hazır - test çağrısı yapmıyoruz (kota tasarrufu)
        api_available = True
        print("✅ Gemini AI başarıyla yapılandırıldı!")
        
    else:
        print("⚠️ Gemini API anahtarı bulunamadı. Demo modu aktif.")
        
except Exception as e:
    print(f"❌ Yapay zeka modeli başlatılamadı: {e}")
    print("📝 Demo modu aktif - Gerçek AI yerine örnek cevaplar kullanılacak.")
    api_available = False
    model = None

def clean_text(text: str) -> str:
    """Metni temizler ve normalize eder."""
    # Fazla boşlukları temizle
    text = re.sub(r'\s+', ' ', text.strip())
    # Özel karakterleri temizle (ama bazılarını koru)
    text = re.sub(r'[^\w\s.,!?;:()-]', '', text)
    return text

def extract_json_from_response(response_text: str) -> dict:
    """AI cevabından JSON formatını çıkarır."""
    try:
        # Markdown kod bloklarını temizle
        clean_response = response_text.strip()
        clean_response = re.sub(r'```json\s*', '', clean_response)
        clean_response = re.sub(r'```\s*', '', clean_response)
        
        # JSON parse et
        return json.loads(clean_response)
    except json.JSONDecodeError:
        # JSON parse edilemezse, metinden bilgi çıkarmaya çalış
        return {"summary": "AI cevabı parse edilemedi.", "keywords": "parse, hata"}

def generate_smart_demo_quiz(text: str, difficulty: str = "medium") -> dict:
    """Metne özel demo quiz oluşturur."""
    words = text.lower().split()
    cleaned_text = clean_text(text)
    
    # Metinden anahtar kelimeler çıkar
    important_words = []
    for word in words:
        if len(word) > 4 and word.isalpha():
            important_words.append(word)
    
    # Metinle ilgili dinamik sorular oluştur
    quiz_questions = []
    
    # Soru 1: Metin uzunluğu temelli
    word_count = len(words)
    if word_count < 100:
        text_type = "kısa bir metin"
    elif word_count < 500:
        text_type = "orta uzunlukta bir metin"
    else:
        text_type = "uzun ve detaylı bir metin"
    
    quiz_questions.append({
        "question": f"Bu metin kaç kelime civarındadır?",
        "options": [f"{word_count-20}-{word_count+20} kelime arası", "10-50 kelime arası", "1000+ kelime", "5-10 kelime arası"],
        "correct_answer": f"{word_count-20}-{word_count+20} kelime arası",
        "explanation": f"Metin yaklaşık {word_count} kelimedir ve {text_type} kategorisindedir."
    })
    
    # Soru 2: İlk paragraf/cümle temelli
    first_sentence = cleaned_text.split('.')[0] if '.' in cleaned_text else cleaned_text[:100]
    quiz_questions.append({
        "question": "Metnin başlangıcında hangi konuya değinilmektedir?",
        "options": ["Ana konuya giriş", "Sonuç bölümü", "Örnek vaka inceleme", "Referans listesi"],
        "correct_answer": "Ana konuya giriş",
        "explanation": f"Metin şu şekilde başlıyor: '{first_sentence[:50]}...'"
    })
    
    # Soru 3: Kelime varlığı temelli
    if important_words:
        sample_word = important_words[0] if important_words else "kelime"
        quiz_questions.append({
            "question": f"Metinde '{sample_word}' gibi anahtar kelimeler hangi amaçla kullanılmıştır?",
            "options": ["Konuyu detaylandırmak için", "Sadece süsleme için", "Sayfa doldurmak için", "Rastgele seçilmiş"],
            "correct_answer": "Konuyu detaylandırmak için",
            "explanation": f"'{sample_word}' gibi kelimeler metnin ana konusunu desteklemektedir."
        })
    
    # Soru 4: Metin türü temelli
    if any(word in text.lower() for word in ['tarih', 'yıl', 'dönem', 'zaman']):
        topic_type = "tarihsel"
    elif any(word in text.lower() for word in ['fen', 'bilim', 'deney', 'sonuç']):
        topic_type = "bilimsel"
    elif any(word in text.lower() for word in ['edebiyat', 'şiir', 'roman', 'yazar']):
        topic_type = "edebi"
    else:
        topic_type = "genel bilgi"
    
    quiz_questions.append({
        "question": "Bu metin hangi alana aittir?",
        "options": [topic_type.title(), "Spor", "Teknoloji", "Mutfak"],
        "correct_answer": topic_type.title(),
        "explanation": f"Metindeki kelimeler ve konu {topic_type} alanına işaret etmektedir."
    })
    
    # Soru 5: Zorluk seviyesine göre
    if difficulty == "easy":
        question_count = 3
    else:
        question_count = min(5, len(quiz_questions))
    
    return {
        "quiz": quiz_questions[:question_count],
        "mode": "smart_demo",
        "analyzed_words": len(important_words),
        "text_length": word_count
    }

def generate_demo_response(text: str, user_level: str = "teen") -> dict:
    """Demo modu için akıllı cevap üretir."""
    words = text.split()
    word_count = len(words)
    cleaned_text = clean_text(text)
    
    # Metinden akıllı özet oluştur
    sentences = [s.strip() for s in cleaned_text.split('.') if s.strip()]
    first_sentence = sentences[0] if sentences else cleaned_text[:100]
    
    # Konu türünü belirle
    text_lower = text.lower()
    if any(word in text_lower for word in ['tarih', 'yıl', 'dönem', 'savaş', 'çağ']):
        topic_type = "tarih"
        smart_summary = f"Bu metin tarihsel bir konuyu ele almaktadır. {first_sentence[:80]}... gibi önemli noktalar üzerinde durmaktadır. Metinde belirtilen tarihsel olaylar ve dönemler konunun anlaşılmasında kritik rol oynamaktadır."
    elif any(word in text_lower for word in ['fen', 'bilim', 'deney', 'kimya', 'fizik', 'biyoloji']):
        topic_type = "bilim"
        smart_summary = f"Bu metin bilimsel bir konuyu açıklamaktadır. {first_sentence[:80]}... şeklinde başlayan açıklamalar konunun temellerini oluşturmaktadır. Bilimsel kavramlar ve süreçler detaylı şekilde ele alınmıştır."
    elif any(word in text_lower for word in ['edebiyat', 'şiir', 'roman', 'yazar', 'eser']):
        topic_type = "edebiyat"
        smart_summary = f"Bu metin edebi bir konuyu incelemektedir. {first_sentence[:80]}... ile başlayan analiz, eserin önemli yönlerini ortaya koymaktadır. Edebi teknikler ve yazarın üslubu detaylı olarak ele alınmıştır."
    else:
        topic_type = "genel"
        smart_summary = f"Bu metin {first_sentence[:80]}... şeklinde başlamaktadır. İçerikte sunulan bilgiler konunun farklı yönlerini ele almakta ve okuyucuya kapsamlı bir bakış açısı sunmaktadır."
    
    # Metne özel anahtar kelimeler üret
    words_lower = [w.lower() for w in words]
    important_words = []
    
    # Uzun ve anlamlı kelimeleri seç
    for word in words_lower:
        if len(word) > 4 and word.isalpha() and word not in ['metin', 'bilgi', 'konu', 'şekilde', 'olarak', 'bunun', 'bu', 've', 'ile', 'için', 'olan', 'olarak', 'yapılan', 'edilen']:
            if word not in important_words:
                important_words.append(word)
                if len(important_words) >= 8:
                    break
    
    # Eksikse genel kelimeler ekle
    if len(important_words) < 5:
        general_keywords = [topic_type, "analiz", "kavram", "açıklama", "örnek", "sonuç", "değerlendirme"]
        for kw in general_keywords:
            if kw not in important_words:
                important_words.append(kw)
                if len(important_words) >= 7:
                    break
    
    keywords = ', '.join(important_words[:7])
    
    # Yaş grubuna göre ayarla
    if user_level == "child":
        smart_summary = f"Bu metinde {topic_type} konusu anlatılıyor. {first_sentence[:50]}... gibi önemli bilgiler var. Metni okuyarak yeni şeyler öğrenebilirsin."
        keywords = "öğrenme, bilgi, önemli, basit, kolay"
    
    return {
        "summary": smart_summary,
        "keywords": keywords,
        "mode": "smart_demo",
        "word_count": word_count,
        "user_level": user_level,
        "topic_type": topic_type
    }

def enhanced_summarize_and_get_keywords(text: str, user_level: str = "teen") -> dict:
    """Gelişmiş metin özetleme ve anahtar kelime çıkarma."""
    global api_available, model
    
    # Giriş kontrolü
    if not text or len(text.strip()) < 10:
        return {
            "summary": "Çok kısa metin, özetlenecek yeterli içerik yok.", 
            "keywords": "kısa, metin",
            "mode": "error",
            "word_count": 0
        }
    
    # Metni temizle
    clean_text_content = clean_text(text)
    word_count = len(clean_text_content.split())
    
    # Demo modu - API yoksa veya model çalışmıyorsa
    if not api_available or not model or not Config.GEMINI_API_KEY:
        return generate_demo_response(clean_text_content, user_level)
    
    # Gerçek AI analizi dene
    try:
        # Yaş grubuna özel prompt ayarları
        if user_level == "child":
            complexity = "Çok basit ve anlaşılır dilde, 7-12 yaş grubu için uygun"
            summary_length = "30-40 kelime"
        else:
            complexity = "Orta seviye karmaşıklıkta, 13+ yaş grubu için uygun"
            summary_length = "50-70 kelime"
        
        prompt = f"""
        Aşağıdaki metni analiz et ve iki görev gerçekleştir:
        
        1. METİN ÖZETİ:
        - {complexity} şekilde özetle
        - Yaklaşık {summary_length} kullan
        - Ana fikirleri ve önemli detayları koru
        - Öğrencinin kolayca anlayacağı şekilde yaz
        
        2. ANAHTAR KELİMELER:
        - En önemli 5-7 anahtar kelimeyi belirle
        - Virgülle ayırarak listele
        - Türkçe karşılıklarını kullan
        
        SADECE JSON formatında yanıtla:
        {{"summary": "...", "keywords": "kelime1, kelime2, kelime3"}}
        
        Analiz edilecek metin:
        ---
        {clean_text_content}
        ---
        """
        
        response = model.generate_content(prompt)
        
        if not response or not response.text:
            raise Exception("API'dan boş cevap geldi")
            
        result = extract_json_from_response(response.text)
        
        # Sonucu doğrula ve zenginleştir
        if not result.get('summary') or result['summary'] in ['Özet oluşturulamadı.', 'AI cevabı parse edilemedi.']:
            raise Exception("Geçerli özet oluşturulamadı")
            
        result["mode"] = "ai"
        result["word_count"] = word_count
        result["user_level"] = user_level
        
        return result
        
    except Exception as e:
        print(f"🔴 AI özetleme hatası: {e}")
        # Quota hatası varsa global değişkenleri güncelle
        if "quota" in str(e).lower() or "429" in str(e):
            api_available = False
            model = None
            print("🚫 Quota bitti - Demo moda geçildi")
        # Hata durumunda demo moduna geç
        return generate_demo_response(clean_text_content, user_level)

def generate_enhanced_quiz_from_text(text: str, difficulty: str = "medium") -> dict:
    """Gelişmiş quiz oluşturma sistemi."""
    global api_available, model
    
    # Demo modu - API yoksa
    if not api_available or not model or not Config.GEMINI_API_KEY:
        return generate_smart_demo_quiz(text, difficulty)
    
    # Gerçek AI quiz oluşturma
    try:
        if difficulty == "easy":
            question_count = 3
            complexity = "basit ve kolay"
        elif difficulty == "hard":
            question_count = 5
            complexity = "zorlu ve analitik"
        else:
            question_count = 5  # Medium için de 5 soru
            complexity = "orta seviye"
        
        prompt = f"""
        Aşağıdaki metni dikkatli bir şekilde analiz et ve {question_count} adet {complexity} çoktan seçmeli test sorusu oluştur.

        SORU KRİTERLERİ:
        ✅ Her soru metnin farklı önemli bölümlerinden olmalı
        ✅ Sorular metinde GERÇEKTEN yer alan bilgilerden oluşmalı
        ✅ Çeldirici şıklar mantıklı ve gerçekçi olmalı
        ✅ Doğru cevap açıklaması metnin hangi kısmından geldiğini belirtmeli
        ✅ Farklı soru tipleri kullan: tanım, sebep-sonuç, karşılaştırma, analiz

        SORU TİPLERİ ÖRNEKLERİ:
        - "Metinde bahsedilen... nedir?"
        - "...hangi nedenle oluşur?"
        - "Aşağıdakilerden hangisi... özelliklerinden biridir?"
        - "Metne göre... ve ... arasındaki fark nedir?"
        - "Yazara göre en önemli nokta hangisidir?"

        SADECE JSON formatında yanıtla, başka metin ekleme:
        [
            {{
                "question": "Metne dayalı soru metni?",
                "options": ["Gerçekçi şık 1", "Gerçekçi şık 2", "Gerçekçi şık 3", "Gerçekçi şık 4"],
                "correct_answer": "Doğru olan şık",
                "explanation": "Bu cevap doğrudur çünkü metinde 'alıntı kısmı' şeklinde bahsedilmektedir."
            }}
        ]

        ANALİZ EDİLECEK METİN:
        ---
        {clean_text(text)}
        ---
        """
        
        response = model.generate_content(prompt)
        quiz_data = json.loads(extract_json_from_response(response.text))
        return {"quiz": quiz_data, "mode": "ai", "difficulty": difficulty}
        
    except Exception as e:
        print(f"🔴 AI quiz oluşturma hatası: {e}")
        # Quota hatası varsa global değişkenleri güncelle
        if "quota" in str(e).lower() or "429" in str(e):
            api_available = False
            model = None
            print("🚫 Quota bitti - Demo moda geçildi")
        
        # Demo quiz döndür (artık api_available False olduğu için recursive olmayacak)
        return generate_smart_demo_quiz(text, difficulty)

# Eski fonksiyonları koruyalım (geriye uyumluluk için)
def summarize_and_get_keywords(text: str) -> dict:
    """Eski API - geriye uyumluluk için."""
    return enhanced_summarize_and_get_keywords(text, "teen")

def generate_quiz_from_text(text: str) -> dict:
    """Eski API - geriye uyumluluk için."""
    result = generate_enhanced_quiz_from_text(text, "medium")
    if "quiz" in result:
        return result
    else:
        return {"error": result.get("error", "Quiz oluşturulamadı.")}