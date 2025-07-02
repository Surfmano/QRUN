from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(f"flask_qrcode_association.config.{config_name.capitalize()}Config")
    
    # Initialise les extensions sans créer de tables
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    return app
