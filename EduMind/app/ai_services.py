import google.generativeai as genai
from config import Config

# API anahtarını yapılandır
try:
    genai.configure(api_key=Config.GEMINI_API_KEY)
    # Modelin yapılandırması
    generation_config = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    # Güvenlik ayarları
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash", # Sizin curl komutunuzdaki model adı
        generation_config=generation_config,
        safety_settings=safety_settings
    )
except Exception as e:
    print(f"Yapay zeka modeli başlatılamadı: {e}")
    model = None

def summarize_and_get_keywords(text: str) -> dict:
    """Verilen metni özetler ve anahtar kelimeler çıkarır."""
    if not model:
        return {"summary": "AI servisi aktif değil.", "keywords": "yok"}

    prompt = f"""
    Aşağıdaki metni analiz et ve iki görev gerçekleştir:
    1. Metni bir öğrencinin kolayca anlayacağı şekilde, yaklaşık 50-60 kelime ile özetle.
    2. Metindeki en önemli 5 anahtar kelimeyi virgülle ayırarak listele.

    İstenen formatta bir JSON nesnesi döndür: {{"summary": "...", "keywords": "..."}}

    Metin:
    ---
    {text}
    ---
    """
    try:
        response = model.generate_content(prompt)
        # Bazen cevap JSON formatı yerine markdown içinde ```json ... ``` olarak gelebilir.
        clean_response = response.text.strip().replace('```json', '').replace('```', '')
        import json
        result = json.loads(clean_response)
        return result
    except Exception as e:
        print(f"AI özetleme hatası: {e}")
        return {"summary": "Özet oluşturulurken bir hata oluştu.", "keywords": "hata"}


def generate_quiz_from_text(text: str) -> dict:
    """Verilen metinden çoktan seçmeli bir sınav oluşturur."""
    if not model:
        return {"error": "AI servisi aktif değil."}

    prompt = f"""
    Aşağıdaki metne dayanarak 3 adet çoktan seçmeli soru oluştur. Her sorunun 4 seçeneği olmalı ve sadece bir tanesi doğru olmalı.
    Doğru cevabı 'correct_answer' anahtarı ile belirt.

    İstenen formatta bir JSON listesi döndür: 
    [
        {{"question": "Soru 1?", "options": ["A", "B", "C", "D"], "correct_answer": "C"}},
        {{"question": "Soru 2?", "options": ["A", "B", "C", "D"], "correct_answer": "A"}}
    ]

    Metin:
    ---
    {text}
    ---
    """
    try:
        response = model.generate_content(prompt)
        clean_response = response.text.strip().replace('```json', '').replace('```', '')
        import json
        quiz_data = json.loads(clean_response)
        return {"quiz": quiz_data}
    except Exception as e:
        print(f"AI quiz oluşturma hatası: {e}")
        return {"error": "Quiz oluşturulurken bir hata oluştu."}