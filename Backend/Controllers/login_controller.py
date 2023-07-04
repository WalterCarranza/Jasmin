from flask import request, jsonify
from werkzeug.security import check_password_hash
from Models.login_model import User
from Config.database import session

def login():
    try:
        # Obtener datos del cuerpo de la solicitud
        username = request.json.get('username')
        password = request.json.get('password')

        # Instancia de la conexion con la base de datos
        Session = session()
        # Buscar al usuario en la base de datos
        user = Session.query(User).filter_by(username = username).first()

        if not user:
            return jsonify({'message': 'Usuario no encontrado'}), 404

        # Verificar la contraseña
        if not check_password_hash(user.password, password):
            return jsonify({'message': 'Contraseña incorrecta'}), 401

        # Realizar acciones adicionales de autenticación y autorización si es necesario

        # Retornar una respuesta exitosa
        return jsonify({'message': 'Inicio de sesión exitoso'}), 200

    except Exception as e:
        return jsonify({'message': 'Error en el servidor'}), 500

def register_user():
    try:
        # Obtener datos del cuerpo de la solicitud
        username = request.json.get('username')
        password = request.json.get('password')

        Session = session()
        # Verificar si el usuario ya existe en la base de datos
        existing_user = Session.query(User).filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': 'El nombre de usuario ya está en uso'}), 400

        return jsonify({'message': 'Usuario registrado exitosamente'}), 201

    except Exception as e:
    #     DatabaseManager.db_sesion.rollback()
        return jsonify({'message': 'Error al registrar el usuario'}), 500
