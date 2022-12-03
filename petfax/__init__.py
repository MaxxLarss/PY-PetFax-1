from flask import Flask

def create_app():
    app = Flask(__name__)


    @app.route('/')
    def hello():
        return "hello, petfax! or whatever"

    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(face.bp)

    return app