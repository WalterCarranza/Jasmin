# create_engine para crear una instancia de la clase Engine que representa la conexión con la BD
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
# from Models.register_model import Register
# from Models.register_model import Register
from Config.config import DIALECT, USER, PASSWORD, HOST, DB, POOL
# from Models.register_model import Register

try:
    # crea la cadena de conexión a la base de datos
    DB_URI = f"{DIALECT}://{USER}:{PASSWORD}@{HOST}/{DB}"
    # Crea la instancia del motor a la BD
    engine = create_engine(DB_URI)
    # Para administrar el ciclo de vida de las conexiones de forma automatica
    Session = sessionmaker(bind=engine)
    session = scoped_session(Session)
    # Se crea la instancia de la clase declarative_base
    Base = declarative_base()
    print("Conexión establecida", session)

except Exception as e:
    # Si se produce algún error, indica que hubo un problema en la conexión
    print("Error en la conexión:", str(e))
