from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from flask_qrcode_association.auth import auth as auth_blueprint
    from flask_qrcode_association.members import members as members_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(members_blueprint)

    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))
    
    return app
