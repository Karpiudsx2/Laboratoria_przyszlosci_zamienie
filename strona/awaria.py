from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from wtforms import FileField, SubmitField, StringField, Form, validators, SelectField, TextAreaField, DateField
from wtforms.validators import ValidationError, StopValidation
from flask_wtf import FlaskForm
from .functions import getting_classroom
from flask_mail import Message
from .models import User
from . import mail
from datetime import date

mal = Blueprint("mal", __name__)


@mal.route("/malfunction", methods=["GET", "POST"])
@login_required
def malfunction():
    class MalfunctionForm(Form):
        person = StringField('Imię zgłaszającej osoby', [validators.DataRequired()])
        sala = SelectField('Sala, w której znajduje się uszkodzony sprzęt', choices=getting_classroom())
        description = TextAreaField('Opis awarii', [validators.Length(min=3, max=1000), validators.DataRequired()])
        submit = SubmitField('Zgłoś awarię ')

    user = User.query.filter_by(id=current_user.id).first()

    form = MalfunctionForm(request.form, person=user.firstname)
    temat = f"Awaria sprzętu. Szkoła Podstawowa w Sękocinie"
    if request.method == 'POST':
        if form.validate() == False:
            flash('Formularz nie poprawnie wypełniony', category="error")
            return render_template('malfunction.html', form=form, user=current_user)
        else:
            print("wysyłanie")
            msg = Message(temat, sender='karpiniakpiotr@gmail.com', recipients=['karpiowygaj@gmail.com'])
            msg.body = f"Użytkownik {form.person.data} prosi o pomoc w rozwiązaniu problemu.\n" \
                       f"W dniu {date.today()} w sali {form.sala.data} zauważono awarię sprzętu.\n " \
                       f"Opis awaarii:\n" \
                       f"{form.description.data}\n" \
                       f"Dziękuję za pomoc"
            flash('Wiadomość została wysłana', category="success")
            print("1")
            mail.send(msg)
            return redirect(url_for("views.home"))
    elif request.method == 'GET':
        return render_template('malfunction.html', form=form, user=current_user)
