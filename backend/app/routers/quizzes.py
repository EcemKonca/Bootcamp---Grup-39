from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from ..services.auth import get_current_user

router = APIRouter(prefix="/api/quizzes", tags=["quizzes"])

@router.get("/")
async def get_quizzes(current_user: User = Depends(get_current_user)):
    return {"quizzes": [], "message": "Quizler henüz eklenmedi"} 