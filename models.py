from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

class Usuario(Base):
  __tablename__ = 'usuarios'

  id = Column(Integer, primary_key=True)
  name = Column(String, unique= False nullable=False)
  gmail = Column(String, unique= False nullable= True)
  password = Column(String, unique=True, nullable=False)


  tarefas = relationship("Tarefa", back_populates="usuario")

class Tarefa(Base):
  __tablename__ = 'tarefas

  id = Column(Integer, primary_key=True) 
  titulo = Column(String, nullable=False)
  descricao = Column(String)
  status = Column(Enum('Pendente', 'Em_andamento', 'Finalizada', name='status_enum'), default='Pendente')
  prioridade = Column(Enum('Baixa', 'Média', 'Alta', name='prioridade_enum'), default='Baixa') 

  id_usuario = Column(Integer, ForeignKey('usuarios.id'))

  usuario = relationship("Usuario", back_populates="tarefas")
