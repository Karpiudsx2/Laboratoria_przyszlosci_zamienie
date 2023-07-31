# Funkcje odpowiedzialne za autoryzację użytkownika
# Roting stron odpowiedzialnych za logowanie
import uuid

from flask import Blueprint, request, flash, render_template, redirect, url_for
from flask_login import current_user, logout_user, login_required, login_user
from flask_mail import Message
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField, SubmitField, EmailField

from . import db
from . import mail
from .functions import getting_subject
from .models import User, TaughtSubject

auth = Blueprint("auth", __name__, )


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = User.query.filter_by(email=email).first()
            if check_password_hash(user.password, password):
                flash("Logowanie pomyslne", category="sucess")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Nieprawidłowe hasło', category="error")
                return render_template('login.html', user=current_user)
        except AttributeError:
            flash("Użytkownik nie znajduje się w bazie danych", category="error")
    return render_template("login.html", user=current_user)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    class RegistrationForm(Form):
        firstname = StringField('Imię', [validators.Length(min=3, max=25), validators.DataRequired()])
        lastname = StringField('Nazwisko', [validators.Length(min=3, max=25), validators.DataRequired()])
        email = StringField("Email address", [validators.Length(min=6, max=70), validators.DataRequired()])
        subject1 = SelectField(label="Nauczany przedmiot", choices=getting_subject())
        password = PasswordField('Password', [validators.DataRequired()])
        confirm = PasswordField("Powtórz hasło", [validators.DataRequired(),
                                                  validators.EqualTo('password', message="Hasła się nie zgadzają")])
        accept_tos = BooleanField("Zgadzam się na TOS", [validators.DataRequired()])
        submit = SubmitField('Wyślij')

    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        subject = TaughtSubject.query.filter_by(subject=form.subject1.data).first()
        print(subject.id)
        new_user = User(firstname=form.firstname.data,
                        lastname=form.lastname.data,
                        email=form.email.data,
                        subject1=subject,
                        password=generate_password_hash(form.password.data)
                        )

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Rejestracja przebiegła pozytywnie. Możesz się zalogować', category="success")
            return redirect(url_for('auth.login'))
        except exc.IntegrityError:
            flash('Użytkownik jest już w bazie danych', category="error")
            db.session.rollback()
    elif request.method == 'POST' and not form.validate():
        flash("formularz nieporawnie wypełniony", category="error")

    return render_template('signup.html', form=form, user=current_user)


@auth.route('/forget', methods=['GET', 'POST'])
def forget():
    server_adress = request.environ['SERVER_NAME']
    server_adress = f'{server_adress}:5000'

    class ForgotForm(Form):
        email = EmailField('Adres mailowy', [validators.DataRequired(), validators.Email()])
        submit = SubmitField('Wyślij')

    form = ForgotForm(request.form)
    if form.validate():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        temat = f'Zmiana Hasła. Laboratoria Przyszłości S.P Sękocin'
        if user:
            code = str(uuid.uuid4())
            user.reset_password = code
            db.session.commit()
            print(user.email)
            msg = Message(temat, sender='karpiniakpiotr@gmail.com', recipients=[user.email])
            msg.body = f"Przekopiuj poniższy link do przeglądarki .\n " \
                       f"{server_adress}/forget/{code}"
            mail.send(msg)
            flash("Link do zmiany hasła został wysłany", category="success")

            return redirect(url_for("views.home"))
        else:
            flash("Nie ma takiego użytkownika", category="error")
    return render_template("forget.html", user=current_user, form=form)


@auth.route('/forget/<string:id>', methods=['GET', 'POST'])
def reset(id):
    print("resetowanie hasła")

    class PasswordResetForm(Form):
        password = PasswordField('Password', [validators.DataRequired()])
        confirm = PasswordField("Powtórz hasło", [validators.DataRequired(),
                                                  validators.EqualTo('password', message="Hasła się nie zgadzają")])
        submit = SubmitField('Zmień hasło')

    user = User.query.filter_by(reset_password=id).first()
    if not user:
        flash("Coś poszło nie tak :(", category="error")
        return redirect(url_for("views.home"))

    form = PasswordResetForm(request.form)

    if user:
        print(user)
        if request.method == "POST":
            password = generate_password_hash(form.password.data)
            print(password)
            user.password = password
            print(user.password)
            user.reset_password = None
            print(user.reset_password)
            db.session.commit()
            flash("Hasło zostało pomyślnie zmienione", category="success")
            return redirect(url_for("views.home"))

    return render_template("reset.html", user=current_user, form=form)
