from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

class Usuario(Base):
  __tablename__ = 'usuarios'

  id = Column(Integer, primary_key=True)

  tarefas = relationship("Tarefa", back_populates="usuario")

class Tarefa(Base):
  __tablename__ = 'tarefas

  id = Column(Integer, primary_key=True)
  id_usuario = Column(Integer, ForeignKey('usuarios.id'))

  usuario = relationship("Usuario", back_populates="tarefas")
