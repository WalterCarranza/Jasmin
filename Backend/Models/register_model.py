'''
    from sqlalchemy import Column, Integer, String: Esta línea importa las clases Column, 
    Integer y String del módulo sqlalchemy. Estas clases se utilizan para definir los 
    campos de una tabla en la base de datos.
'''
from sqlalchemy import Column, Date, Integer, String, LargeBinary, Boolean
from Config.database import Base
from sqlalchemy.orm import relationship
from Models.login_model import User

class Register(Base):
    __tablename__ = 'register'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=True)
    photo = Column(LargeBinary, nullable=True)
    is_delete = Column(Boolean, nullable=False, default=False)

    user = relationship("User", back_populates="register")

    def __init__(self, first_name, last_name, email, password, birth_date, photo):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.photo = photo

    def __repr__(self):
        return f'Register({self.id}, {self.first_name}, {self.last_name}, {self.email}, {self.password}, {self.birth_date})'
    
    def __str__(self):
        return self.first_name