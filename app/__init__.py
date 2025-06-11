from flask import Flask
from .models import db
from .routes import fba
from .seed_data import seed_data

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        seed_data()
        app.register_blueprint(fba)

    return app
