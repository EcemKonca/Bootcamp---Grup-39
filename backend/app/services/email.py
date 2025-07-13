# Email servisi geçici olarak devre dışı

async def send_verification_email(email: str, token: str):
    """Email doğrulama devre dışı"""
    pass

async def send_reset_password_email(email: str, token: str):
    """Şifre sıfırlama emaili devre dışı"""
    pass

def create_verification_token(email: str) -> str:
    """Email doğrulama için token oluştur"""
    return "dummy_token"

def create_password_reset_token(email: str) -> str:
    """Şifre sıfırlama için token oluştur"""
    return "dummy_token"

def verify_token(token: str) -> dict:
    """Token doğrulama"""
    return {"email": "dummy@example.com", "valid": False} 