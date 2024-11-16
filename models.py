from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

class Usuario(Base):
  __tablename__ = 'usuarios'
