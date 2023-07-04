from flask import request, jsonify
from werkzeug.security import generate_password_hash
from Config.database import session
from Models.login_model import User
from Models.register_model import Register
import base64

def add_register():
    try:
        # Verificar si la solicitud es multipart/form-data para el envio de archivos binarios
        if request.content_type.startswith('multipart/form-data'):
            # Obtener los datos del formulario
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            password = request.form.get('password')
            birth_date = request.form.get('birth_date')
            photo = request.files.get('photo')

            # Verificar si el email ya existe en la base de datos
            existing_register = session.query(Register).filter_by(email=email).first()
            if existing_register:
                session.close()
                print("El email ya está registrado")
                return 'El email ya está registrado en la base de datos'

            # Generar el hash de la contraseña
            hashed_password = generate_password_hash(password)

            # Crear una nueva instancia de Register con los datos obtenidos
            new_register = Register(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_password,
                birth_date=birth_date,
                photo=photo.read() if photo else None
            )

            # Guardar la nueva instancia en la base de datos
            session.add(new_register)
            session.commit()

            print("Registro creado exitosamente")

            if new_register:
                register = session.query(Register).filter_by(email=email).first()

                # Obtener el id del registro creado
                register_id = register.id

                # Crear una nueva instancia de User con los datos obtenidos
                new_user = User(
                    username=email,
                    password=hashed_password,
                    register_id=register_id
                )
            
                # Guardar la nueva instancia de User en la base de datos
                session.add(new_user)
                print("Se ha agregado la instancia al registro de login")
                session.commit()
                session.close()
            else:
                print("No se pudo agregar el nuevo registro al login")

            return jsonify({'message': 'Datos agregados correctamente en la base de datos'}), 200
        else:
            # La solicitud no es multipart/form-data
            return jsonify({'message': 'La solicitud no es de tipo multipart/form-data'}), 400

    except Exception as e:
        # En caso de error, retornar un mensaje de error
        return jsonify({'message': 'Error en el servidor'}), 500


    


# Obtener un registro por su id
def get_register_by_id(id):
    try:
        register = session.query(Register).filter(Register.id == id).first()
        if register:
            serialized_register = {
                'id': register.id,
                'first_name': register.first_name,
                'last_name': register.last_name,
                'email': register.email,
                'password': register.password,
                'birth_date': str(register.birth_date),
                'photo': base64.b64encode(register.photo).decode('utf-8') if register.photo else None
            }
            print(register)
            return jsonify(serialized_register), 200
        else:
            return jsonify({'message': 'Register not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500



# Obtener la lista de todos los registros
def get_all_registers():
    try:
        registers = session.query(Register).all()
        result = []
        for register in registers:
            result.append({
                'id': register.id,
                'first_name': register.first_name,
                'last_name': register.last_name,
                'email': register.email,
                'password': register.password,
                'birth_date': str(register.birth_date) if register.birth_date else None,
                'photo': base64.b64encode(register.photo).decode('utf-8') if register.photo else None
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def delete_register_by_id(id):
    try:
        register = session.query(Register).filter(Register.id == id).first()
        if register:
            register.is_delete = True
            session.commit()
        else:
            print("El registro no fue encontrado")

    except Exception as e:
        return jsonify({'error': str(e)}), 500