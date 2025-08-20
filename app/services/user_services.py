"""
Serviço para operações com a tabela glpi_user
"""

from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import select

# Supondo que existe um modelo SQLAlchemy chamado GlpiUser
from app.models.glpi_user import GlpiUser


class UserService:
    """
    Serviço para manipulação de usuários GLPI
    """

    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int) -> Optional[GlpiUser]:
        """Busca usuário pelo ID"""
        return self.db.query(GlpiUser).filter(GlpiUser.id == user_id).first()

    def get_user_by_phone(self, phone: str) -> Optional[GlpiUser]:
        """Busca usuário pelo telefone"""
        return self.db.query(GlpiUser).filter(GlpiUser.phone == phone).first()
