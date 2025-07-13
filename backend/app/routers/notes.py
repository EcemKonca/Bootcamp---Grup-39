from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from ..services.auth import get_current_user

router = APIRouter(prefix="/api/notes", tags=["notes"])

@router.get("/")
async def get_notes(current_user: User = Depends(get_current_user)):
    return {"notes": [], "message": "Notlar henüz eklenmedi"} 