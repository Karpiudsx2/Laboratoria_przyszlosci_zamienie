# models.py przechowuje klasy, które wpsółpracują z ORM.
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user
from sqlalchemy.sql import func
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash

from . import db, app

admin = Admin(app)


class User(db.Model, UserMixin):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    subject1_id = db.Column(db.Integer, db.ForeignKey('TaughtSubject.id'), nullable=False)
    subject2_id = db.Column(db.Integer, db.ForeignKey('TaughtSubject.id'), nullable=True)
    subject3_id = db.Column(db.Integer, db.ForeignKey('TaughtSubject.id'), nullable=True)
    password = db.Column(db.String(150), nullable=False)
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    subject1 = db.relationship("TaughtSubject", foreign_keys=[subject1_id])
    subject2 = db.relationship("TaughtSubject", foreign_keys=[subject2_id])
    subject3 = db.relationship("TaughtSubject", foreign_keys=[subject3_id])
    is_admin = db.Column(db.Boolean, default=False)
    is_managment = db.Column(db.Boolean, default=False)
    reset_password = db.Column(db.String(300), nullable=True)

    def __str__(self):
        return str(self.id)

    def set_password(self, password):
        """Set password"""
        self.password = generate_password_hash(password)


# Tabela słownikowa
class TaughtSubject(db.Model):
    __tablename__ = "TaughtSubject"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return f"{self.subject}"


# Tabela słownikowa
# zawiera numer urządzenia w szkole
class Device(db.Model):
    __tablename__ = "Device"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # numer w szkole
    scholl_id = db.Column(db.String(3), nullable=False)
    kategoria_id = db.Column(db.String(50), db.ForeignKey('Kategoria.id'))
    kategoria = db.relationship("Kategoria", foreign_keys=[kategoria_id])
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    photo = db.Column(db.String(500), nullable=True)

    def __str__(self):
        return f"{self.description}"


class Kategoria(db.Model):
    __tablename__ = "Kategoria"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f"{self.category_name}"


class DeviceUsage(db.Model):
    __tablename__ = "DeviceUsage"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deviceinfo_id = db.Column(db.ForeignKey('Device.id'))
    deviceinfo = db.relationship("Device", foreign_keys=[deviceinfo_id])
    working_hours = db.Column(db.Float, nullable=False)


class Raport(db.Model):
    __tablename__ = "Raport"
    # klucz główny
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # klucze obce
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    deviceusage_id = db.Column(db.Integer, db.ForeignKey('DeviceUsage.id', ondelete="CASCADE"))
    subject = db.Column(db.Integer, db.ForeignKey('TaughtSubject.id'))
    # dodatkowe informacje
    input_date = db.Column(db.DateTime(timezone=True), default=func.now())
    class_date = db.Column(db.DateTime(timezone=True), nullable=False)
    # Tematy w dzienniku lekcyjnym, na potrzeby, którego został użyty sprzęt
    reference = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    uwagi = db.Column(db.String(1000), nullable=True)

    # data potrzebna dla frontu

    def __str__(self):
        return f"{self.class_date}, {self.deviceusage_id}"

    def data(self):
        return f"{str(self.class_date)[0:10]}"


class File(db.Model):
    __tablename__ = "File"
    # klucz główny
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    typ = db.Column(db.String, nullable=False)
    filename = db.Column(db.String, nullable=False)
    raport_id = db.Column(db.Integer, db.ForeignKey('Raport.id'))


class Classroom(db.Model):
    __tablename__ = "Classroom"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    classroom = db.Column(db.String, nullable=False)

    def __str__(self):
        return f"{self.classroom}"


class Malfunction(db.Model):
    __tablename__ = "Malfunctinon"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    description = db.Column(db.Integer, nullable=False)
    take_care = db.Column(db.Boolean, default=False)


# tworzenie widoku admin
class AdminView(ModelView):
    def is_accessible(self):
        if current_user.is_admin:
            return current_user.is_authenticated
        else:
            return abort(404)

    # def on_model_change(self, form, User, is_created):
    #     if form.password.data is not None:
    #         User.set_password(form.password.data)
    #     else:
    #         del form.password


# dodawanie widoków do Admin
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(TaughtSubject, db.session))
admin.add_view(AdminView(Device, db.session))
admin.add_view(AdminView(Kategoria, db.session))
admin.add_view(AdminView(DeviceUsage, db.session))
admin.add_view(AdminView(Raport, db.session))
admin.add_view(AdminView(File, db.session))
