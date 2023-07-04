from flask import Flask, jsonify, make_response
from flask_cors import CORS
from Config import database
from Routes.login_routes import configure_login_routes
from Routes.register_routes import configure_add_register_routes, configure_get_all_register_routes, configure_get_register_routes

app = Flask(__name__)
app.debug = True
CORS(app)

# Cargando las rutas
configure_login_routes(app)
configure_add_register_routes(app)
configure_get_all_register_routes(app)
configure_get_register_routes(app)

app.config['JSON_AS_ASCII'] = False

app.config['SESSION_COOKIE_NAME'] = 'session'
app.config['SECRET_KEY'] = 'COOKIE_SECRET'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'


def run():
    pass


@app.route('/')
def index():
    data = {
        'message': 'Hello, world!',
        'status': 200
    }
    return jsonify(data)


@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Headers", "Origin, Content-Type, Accept")
    return response


if __name__ == '__main__':
    database.Base.metadata.create_all(database.engine)
    app.run(port=8080)
