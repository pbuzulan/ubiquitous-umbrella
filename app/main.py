from flask import Flask
from app.routes import bp

app = Flask(__name__)


def create_app():
    # Additional configuration here

    app.register_blueprint(bp)

    return app
