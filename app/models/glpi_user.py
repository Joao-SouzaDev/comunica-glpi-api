"""
Modelo SQLAlchemy para a tabela glpi_users
"""

from sqlalchemy import Column, Integer, String

from app.database import Base


class GlpiUser(Base):
    __tablename__ = "glpi_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(50), unique=True, nullable=True)
    entities_id = Column(Integer, nullable=False)
    # Adicione outros campos conforme necessário

    def __repr__(self):
        return f"<GlpiUser(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone}', entities_id={self.entities_id})>"
