'''
    from sqlalchemy import Column, Integer, String: Esta línea importa las clases Column, 
    Integer y String del módulo sqlalchemy. Estas clases se utilizan para definir los 
    campos de una tabla en la base de datos.
'''
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from Config.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    
    register_id = Column(Integer, ForeignKey('register.id'), unique=True, nullable=False)
    is_delete = Column(Boolean, nullable=False, default=False)

    register = relationship("Register", back_populates="user")

    def __init__(self, username, password, register_id):
        self.username = username
        self.password = password
        self.register_id = register_id

    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.password}, {self.register_id})'
    
    def __str__(self):
        return self.username