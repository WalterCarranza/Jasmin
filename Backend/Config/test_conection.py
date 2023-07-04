from database import session
from Models.register_model import Register


def test_register_crud():
    # Obtener una sesión de base de datos
    Session = session()

    if Session:
        try:
            # CREATE: Agregar un nuevo registro
            new_register = Register(first_name='John', last_name='Doe', email='johndoe@example.com', password='password123', birth_date='1990-01-01')
            Session.add(new_register)
            Session.commit()
            print("Registro agregado exitosamente")

            # READ: Obtener todos los registros
            registers = Session.query(Register).all()
            for register in registers:
                print(register.first_name, register.last_name, register.email)

            # UPDATE: Actualizar un registro existente
            register_to_update = Session.query(Register).filter_by(email='johndoe@example.com').first()
            if register_to_update:
                register_to_update.first_name = 'John Updated'
                session.commit()
                print("Registro actualizado exitosamente")

            # DELETE: Eliminar un registro existente
            register_to_delete = Session.query(Register).filter_by(email='johndoe@example.com').first()
            if register_to_delete:
                session.delete(register_to_delete)
                session.commit()
                print("Registro eliminado exitosamente")

        except Exception as e:
            print("Error:", str(e))
    else:
        print("No se pudo establecer la conexión con la base de datos")
