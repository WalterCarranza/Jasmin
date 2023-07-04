from Controllers.register_controller import add_register, get_all_registers, delete_register_by_id, get_register_by_id

def configure_add_register_routes(app):
    @app.route('/add_register', methods=["POST"])
    def add():
        return add_register()
    
def configure_get_all_register_routes(app):
    @app.route('/get_all_registers', methods=["GET"])
    def all():
        return get_all_registers()
    
def configure_get_register_routes(app):
    @app.route('/get_register/<int:id>', methods=["GET"])
    def get_register_by_id(id):
        return get_register_by_id(id)
    
def configure_delete_register_routes(app):
    @app.route('/delete_register/<int:id>', methods=["PUT"])
    def delete_register_by_id(id):
        return delete_register_by_id()
