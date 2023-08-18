import os
import uuid
from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import FileField, ValidationError
from wtforms import StringField, SelectField, SubmitField, HiddenField
from .functions import *
from .models import Raport, DeviceUsage, File

# przy uplodowaniu na pythonanywhere trzeba tą ściężkę poprawić
sciezka = path.join(getcwd(), "strona", "static", "raportphotos")
views = Blueprint("views", __name__)


class UploadFileForm(FlaskForm):
    file = FileField(label="File")
    submit = SubmitField(label="Upload File")


@views.route('/', methods=['GET', 'POST'])
def home():
    user = current_user
    if not user.is_authenticated:
        return redirect(url_for("auth.login"))
    else:
        return render_template("home.html", user=current_user)


@views.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    return render_template('upload.html')


@views.route('/equipment', methods=['GET'])
@login_required
def equipment():
    lista = db.session.query(Device.scholl_id, Device.name, Device.description, Device.photo).all()
    lista = [list(i) for i in lista]
    for item in lista:
        item[3] = '/devicephotos/' + str(item[3])
    return render_template('equipment.html', user=current_user, list=lista)


@views.route('/report', methods=['GET', 'POST'])
@login_required
def report():
    check = True
    formularz = []
    lista = getting_device_list()
    if request.method == "POST":

        name = request.form.get("name")
        formularz.append(name)
        device_name = []
        device_name.append(request.form.get("device"))
        formularz.append(device_name)
        lname = request.form.get("Lname")
        formularz.append(lname)
        data = request.form.get("date")
        if not data:
            check = False
        else:
            data = datetime.strptime(data, '%Y-%m-%d')
            data = data.date()
        file = request.files.getlist("file[]")

        subject = request.form.get("przedmiot")
        formularz.append(subject)
        description = request.form.get("description")
        formularz.append(description)
        reference = request.form.get('reference')
        formularz.append(reference)
        working_hours = request.form.get('working_hours')
        formularz.append(working_hours)
        if formularz.count(None) > 0:
            check = False
        else:
            for element in formularz:
                if len(element) == 0:
                    check = False

        if check:
            # potrzebne do skonstruowania relacji w sqlalachemyh
            device = Device.query.filter_by(name=device_name[0]).first()
            print(device_name)
            print(device)

            # wstawianie do bazy danych DeviceUsage
            new_deviceusage = DeviceUsage(deviceinfo_id=device.id, working_hours=working_hours)
            db.session.add(new_deviceusage)
            db.session.flush()
            db.session.refresh(new_deviceusage)

            # wyszukiwanie przedmiotu
            subject = TaughtSubject.query.filter_by(subject=subject).first()
            new_raport = Raport(user_id=current_user.id, deviceusage_id=new_deviceusage.id, subject=subject.id,
                                class_date=data, reference=reference, description=description)
            db.session.add(new_raport)
            db.session.flush()
            db.session.refresh(new_raport)

            if all(file):
                for f in file:
                    name, extension = path.splitext(f.filename)
                    unique_filename = f'{str(uuid.uuid4())}{extension}'
                    path_to_save = os.path.join(sciezka, unique_filename)
                    f.save(path_to_save)
                    file_to_resize = path_to_save
                    resize_picture(file_to_resize)
                    # korzystamy z klasy File
                    new_file = File(typ="image", filename=unique_filename, raport_id=new_raport.id)
                    db.session.add(new_file)
                    db.session.commit()
                    flash("formularz poprawnie wypełniony", category="success")
            db.session.commit()
            return redirect(url_for("views.home"))
        else:
            flash("formularz niepoprawnie wypełniony", category="error")

    return render_template('report.html', lista=lista, user=current_user, subject_list=getting_subject())


@views.route('/report/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_report(id):
    report = db.session.query(Raport, DeviceUsage, Device, TaughtSubject) \
        .select_from(Raport) \
        .join(DeviceUsage) \
        .join(Device) \
        .join(TaughtSubject) \
        .filter(Raport.id == id) \
        .order_by(desc(Raport.input_date)) \
        .all()

    files = db.session.query(File).filter(File.raport_id == id).all()
    lista = []
    for f in files:
        lista.append("raportphotos/" + f.filename)

    if request.method == "POST":
        formularz = ChangeReportFormData(request, current_user)
        if formularz.validate():
            formularz.change_report(id)
            db.session.commit()
            flash("raport poprawnie zmieniono", category="success")
            return redirect(url_for('views.myraports'))
        elif not formularz.validate():
            flash("formularz niepoprawnie wypełniony", category="error")

    return render_template('edit_report.html', user=current_user, report=report, lista=getting_device_list(),
                           subject=getting_subject(), files=lista)


@views.route('/report/delete/<int:id>', methods=["GET", "POST"])
@login_required
def delete_raport(id):
    report = Raport.query.filter_by(id=id).first()
    if report:
        try:
            Raport.query.filter_by(id=id).delete()
            delete_file_row(id)
            DeviceUsage.query.filter_by(id=report.deviceusage_id).delete()
            db.session.commit()
            flash("Raport usunięty", category="success")
        except:
            db.session.rollback()
            flash("Coś poszło nie tak ;(", category="error")

        return redirect(url_for('views.myraports'))
    else:
        return "<h1>nie ma takiego raportu</h1>"


@views.route('/editdata', methods=["GET", "POST"])
@login_required
def editdata():
    class ChangeDataForm(Form):
        hidden_field = HiddenField("Change_data")
        firstname = StringField('Imię', [validators.Length(min=3, max=25), validators.DataRequired()])
        lastname = StringField('Nazwisko', [validators.Length(min=3, max=25), validators.DataRequired()])
        email = StringField("Email address", [validators.Length(min=6, max=35), validators.DataRequired()])
        submit = SubmitField('Zmień dane')
        submit.data = False

    class ChangeSubjectForm(Form):
        subject1 = SelectField("Nauczany przedmiot 1", choices=getting_subject())
        subject2 = SelectField("Nauczany przedmiot 2", choices=getting_subject())
        subject3 = SelectField("Nauczany przedmiot 3", choices=getting_subject())
        submit = SubmitField('Zmień przedmiot')
        submit.data = False

        def validate_subject1(self, subject1):
            if subject1 == "---":
                raise ValidationError("Proszę wybrać przynajmniej 1 przedmiot lub pozycje: inne")

    class AddSchedule(Form):
        przedmiot = SelectField("Nauczany przedmiot", choices=getting_subject())
        grade = SelectField("Wybierz klasę", choices=[x for x in range(1, 9)])
        name = StringField("Podaj nazwę podręcznika")
        wydawnictwo = StringField("Wpisz wydawnictwo")
        plik = FileField('wskaż plik csv')
        submit = SubmitField('Dodaj podręcznik')

    class ChangePasswordForm(Form):
        hidden_field = HiddenField("Change_password")
        current_password = PasswordField('Obecne hasło')
        password = PasswordField('Password', [validators.DataRequired()])
        confirm = PasswordField("Powtórz hasło", [validators.DataRequired(),
                                                  validators.EqualTo('password', message="Hasła się nie zgadzają")])
        submit = SubmitField('Zmień hasło')
        submit.data = False

        def validate_current_password(self, current_password):
            user = User.query.filter_by(id=current_user.id).first()
            if not check_password_hash(user.password, current_password.data):
                raise ValidationError("Obecne hasło jest nieprawidłowe")

    form = ChangeDataForm(request.form)
    form2 = ChangeSubjectForm(request.form,
                              subject1=getting_taught_subjects(current_user.id, 1),
                              subject2=getting_taught_subjects(current_user.id, 2),
                              subject3=getting_taught_subjects(current_user.id, 3)
                              )
    form3 = AddSchedule(request.form)
    form4 = ChangePasswordForm(request.form)

    if request.method == "POST":

        if request.form['submit'] == 'Zmień dane' and form.validate():
            user = User.query.filter_by(id=current_user.id).first()
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
            user.email = form.email.data
            db.session.commit()
            flash("Dane pomyslnie zmienione", category="success")

        if request.form['submit'] == 'Zmień przedmiot':
            user = User.query.filter_by(id=current_user.id).first()
            subject = TaughtSubject.query.filter_by(subject=form2.subject1.data).first()
            user.subject1 = subject
            if form2.subject2.data == "---":
                form2.subject2.data = None
            subject2 = TaughtSubject.query.filter_by(subject=form2.subject2.data).first()
            user.subject2 = subject2
            if form2.subject3.data == "---":
                form2.subject3.data = None
            subject3 = TaughtSubject.query.filter_by(subject=form2.subject3.data).first()
            user.subject3 = subject3
            try:
                db.session.commit()
                flash("Dane pomyslnie zmienione", category="success")
            except:
                db.session.rollback()

        # if request.form['submit'] == 'Dodaj podręcznik':
        #     przedmiot = form3.przedmiot.data
        #     grade = form3.grade.data
        #     wydawnictwo = form3.wydawnictwo.data
        #     nazwa = form3.name.data
        #     file = form3.plik.data
        #     try:
        #         pass
        #     except OSError:
        #         flash("Rozkład materiałów już istnieje", category="error")

        if request.form['submit'] == 'Zmień hasło' and form4.validate():
            user = User.query.filter_by(id=current_user.id).first()
            user.password = generate_password_hash(form4.password.data)
            db.session.commit()
            flash("Hasło zmieniono pomyślnie", category="success")

    return render_template('editdata.html', user=current_user, form=form, form2=form2, form3=form3, form4=form4)


@views.route('/usage', methods=["GET"])
@login_required
def usage():
    suma = SummaryUsage()
    return render_template("usage.html", user=current_user, hours_by_user=suma.count_hours_by_user(),
                           hours_by_category=suma.count_hours_by_category(), lista=suma.summary(),
                           count=suma.list_length(),
                           suma=suma.count_hours())


@views.route('/myraports', methods=["Get", "POST"])
@login_required
def myraports():
    raports = db.session.query(Raport, DeviceUsage, Device) \
        .select_from(Raport) \
        .join(DeviceUsage) \
        .join(Device) \
        .filter(Raport.user_id == current_user.id) \
        .order_by(desc(Raport.input_date)) \
        .all()

    return render_template('myraports.html', user=current_user, raports=raports)


@views.route("/confirm/<id>", methods=["GET", "POST"])
@login_required
def confirm(id):
    return render_template('confirm.html', user=current_user, id=id)


@views.route("/raporty", methods=["GET", "POST"])
@login_required
def raporty():
    raports = db.session.query(Raport, DeviceUsage, Device, User) \
        .select_from(Raport) \
        .join(DeviceUsage) \
        .join(Device) \
        .join(User) \
        .order_by(desc(Raport.input_date)) \
        .all()

    files = db.session.query(File).all()

    return render_template("statystyki.html", user=current_user, raports=raports, files=files)
