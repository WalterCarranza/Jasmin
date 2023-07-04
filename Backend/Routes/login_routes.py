from Controllers.login_controller import login
from Controllers.login_controller import register_user

def configure_login_routes(app):
    @app.route('/login', methods=["POST"])
    def get_login():
        return login()


# def configure_register_routes(app):

#     @app.route("/register", methods=["POST"])
#     def get_registers():
#         return register_user()

