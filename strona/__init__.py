from os import path
from flask import Flask, session
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

db = SQLAlchemy()
DB_NAME = 'database.db'
mail = Mail()

# Uruchamia serwer WSGI
app = Flask(__name__)

app.secret_key = "Piotr"
app.config['UPLOAD_FOLDER'] = app.static_folder + "/photos"
# konfiguracja ścieżki dostępu do bazy danych
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['UPLOAD_FOLDER'] = app.static_folder + "/devicephotos"
app.config['ENV'] = 'development'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# konfiguracja flask-mail
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USERNAME"] = "karpiniakpiotr@gmail.com"
app.config["MAIL_PASSWORD"] = "qgfgxqnqkgkvtagt"
mail.init_app(app)
db.init_app(app)

from .views import views
from .auth import auth
from .awaria import mal

# from .admin import admin

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")
app.register_blueprint(mal, url_prefix="/")
# app.register_blueprint(admin, url_prefix="/")

from .models import TaughtSubject, User

# DeviceUsage, Raport,

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def create_database(app):
    if not path.exists('strona/' + DB_NAME):
        db.create_all(app=app)


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


create_database(app)  # sprawdza czy istnieje wcześniej utworzona baza.Jeżeli nie to ją tworzy
