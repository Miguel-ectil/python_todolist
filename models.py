from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

class Usuario(Base):
  __tablename__ = 'usuarios'

  id = Column(Integer, primary_key=True)

class Tarefa(Base):
  __tablename__ = 'tarefas
