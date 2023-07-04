def initial():
    from Models.register_model import Register
    from Models.login_model import User
    from Config.database import session

    # Verificar si el correo electrónico ya existe en la base de datos
    def email_exists(email):
        return session.query(Register).filter_by(email=email).first() is not None

    # Agregar el registro del usuario root y admin si el correo electrónico no existe
    if not email_exists("root@root.com"):
        root = Register(first_name="root", last_name="root", email="root@root.com", password="123456789", birth_date="")
        session.add(root)

        # register_id =session.query(Register).filter_by(id=root.id).first().id
        # root_user = User(username=root.email, password=root.password, register_id=register_id)
        # session.add(root_user)

    if not email_exists("admin@admin.com"):
        admin = Register(first_name="admin", last_name="admin", email="admin@admin.com", password="123456789", birth_date="")
        session.add(admin)

        # admin_user = User(username=admin.email, password=admin.password, register_id=admin.id)
        # session.add(admin_user)

    result = session.query(Register).all()
    print("Obteniendo todos los registros")
    for register in result:
        print(register.id, register.first_name, register.last_name, register.email, register.password, register.birth_date)

    session.commit()
