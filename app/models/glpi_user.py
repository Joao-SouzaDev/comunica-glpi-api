"""
Modelo SQLAlchemy para a tabela glpi_user
"""

from sqlalchemy import Column, Integer, String

from app.database import Base


class GlpiUser(Base):
    __tablename__ = "glpi_user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(50), unique=True, nullable=True)
    profile = Column(String(100), nullable=True)
    # Adicione outros campos conforme necessário

    def __repr__(self):
        return f"<GlpiUser(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone}')>"
        return f"<GlpiUser(id={self.id}, name='{self.name}', email='{self.email}')>"
