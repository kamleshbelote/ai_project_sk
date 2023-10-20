from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from .controller import bp_user, bp_admin
from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_admin)
    jwt.init_app(app=app)
    # db.init_app(app)
    flask_bcrypt.init_app(app)

    return app