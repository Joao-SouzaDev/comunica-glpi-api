"""
Router para operações de usuário GLPI
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user_services import UserService
from app.database import get_db
from app.models.glpi_user import GlpiUser

router = APIRouter(prefix="/users", tags=["Usuários"])


@router.get("/{user_id}", response_model=None)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


@router.get("/email/{email}", response_model=None)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


@router.get("/phone/{phone}", response_model=None)
def get_user_by_phone(phone: str, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user_by_phone(phone)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user
