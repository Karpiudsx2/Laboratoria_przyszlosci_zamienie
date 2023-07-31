import csv
from PIL import Image
from datetime import datetime
from flask import flash
from os import path, getcwd, makedirs
from sqlalchemy import func, desc
from wtforms import Form, EmailField, PasswordField, validators

from strona.models import User, TaughtSubject, Classroom, Raport, File
from . import db
from .models import Device, DeviceUsage, Kategoria


def getting_device_list():
    lista = []
    try:
        devices = Device.query.all()
    except:
        pass
    for device in devices:
        lista.append(device.name)
    return lista


def getting_subject():
    """
    :return: returning list of subject stored in database
    """
    lista = ["---"]
    subject = TaughtSubject.query.all()
    for s in subject:
        lista.append(s.subject)
    return lista


def getting_taught_subjects(userid, subject_number):
    """
    Funkcja zwraca listę zapisanych przedmitów w bazie danych
    """
    user = User.query.filter_by(id=userid).first()
    lista = []

    if user.subject1 is None:
        lista.append("---")
    else:
        lista.append(user.subject1.subject)

    if user.subject2 is None:
        lista.append("---")
    else:
        lista.append(user.subject2.subject)

    if user.subject3 is None:
        lista.append("---")
    else:
        lista.append(user.subject3.subject)
    return lista[subject_number - 1]


def importcsv(file: str):
    try:
        with open(file, encoding="utf8") as csvfile:
            lista = csv.reader(csvfile)
            lista = list(lista)
    except IOError:
        flash("Niepoprawny plik")


def create_path(nazwa_przedmiotu: str, poziom: str, wydawnictwo: str, nazwa_podrecznika: str):
    """
    return: path of created directory
    """
    sciezka = path.join(getcwd(), "strona", "static", "rozklady_materialow", nazwa_przedmiotu, poziom, wydawnictwo,
                        nazwa_podrecznika, )
    makedirs(sciezka)
    return sciezka


def create_report_path():
    """
    return: path of created directory
    """
    sciezka = path.join(getcwd(), "strona", "static", "raportphotos")
    makedirs(sciezka, exist_ok=True)
    return sciezka


def add_path_to_db(raport_id: int, filename: str):
    sciezka = "raportphotos/Raport" + f'{str(raport_id)}/{filename}'
    return sciezka


def resize_picture(file_path: str):
    """
    :arg file path of image
    :return
    """
    Max_x = Max_y = 320
    image = Image.open(file_path)
    x, y = image.size
    if x > y:
        ratio = x / Max_x
    else:
        ratio = y / Max_y
    x = int(x / ratio)
    y = int(y / ratio)

    image = image.resize((x, y), Image.ANTIALIAS)
    image.save(file_path, optimize=True, quality=95)


def getting_classroom():
    """
    :return: returning list of subject stored in database
    """
    lista = ["---"]
    classroom = Classroom.query.all()
    for c in classroom:
        lista.append(c.classroom)
    return lista


class ChangeReportFormData:
    """
    Class store data from request form
    """

    def __init__(self, request, current_user):
        self.empty_dict = {}
        self.current_user = current_user
        self.name = request.form.get("name")
        self.device = request.form.get("device")
        self.Lname = request.form.get("Lname")
        self.date = request.form.get("date")
        print(request.files.getlist('file[]'))
        if request.files.getlist('file[]'):
            self.files = request.files.getlist('file[]')
        else:
            self.files = None
        self.subject = request.form.get("przedmiot")
        self.description = request.form.get("description")
        self.reference = request.form.get('reference')
        self.working_hours = request.form.get('working_hours')
        self.formularz = {
            "device": self.device,
            "data": self.date,
            "subject": self.subject,
            "description": self.description,
            "reference": self.reference,
            "working_hours": self.working_hours
        }
        # wywoływanie metod pomocniczcych
        self.empty()
        self.convertdate()

    def dict(self):
        return self.formularz

    def empty(self):
        for key in self.formularz:
            if not self.formularz[key]:
                self.empty_dict = {
                    key: self.formularz[key]
                }
        return self.empty_dict

    def validate(self):
        return all(self.formularz.values())

    def convertdate(self):
        """
        :return function change time to datetime format if validate
        """
        if self.validate():
            data = datetime.strptime(self.date, '%Y-%m-%d')
            data = data.date()
            self.date = data
        return None

    def create_report_path(self, raport_id: int):
        """
        return: path of created directory
        """
        if not self.raport:
            sciezka = path.join(getcwd(), "strona", "static", "raportphotos", "Raport" + str(raport_id))
            makedirs(sciezka, exist_ok=True)
            return sciezka
        else:
            return None

    def db_path(self, id):
        """
        :return add path to db
        """
        lista = []
        if self.files:
            for element in self.files:
                lista.append("raportphotos/Raport" + f'{str(id)}/{element.filename}')
        print(lista)
        return str(lista)

    def create_raport(self):
        device = Device.query.filter_by(name=self.device).first()
        # wstawianie do bazy danych DeviceUsage
        new_deviceusage = DeviceUsage(deviceinfo_id=device.id, working_hours=self.working_hours)
        db.session.add(new_deviceusage)
        db.session.flush()
        db.session.refresh(new_deviceusage)
        # wyszukiwanie przedmiotu
        subject = TaughtSubject.query.filter_by(subject=self.subject).first()
        new_raport = Raport(user_id=self.current_user.id, deviceusage_id=new_deviceusage.id, subject=subject.id,
                            class_date=self.date, reference=self.reference, description=self.description, file_path="")
        db.session.add(new_raport)
        db.session.flush()
        db.session.refresh(new_raport)
        new_raport.img_src = self.create_report_path(new_raport.id)
        for file in self.files:
            path_to_save = path.join(new_raport.img_src, file.filename)
            file.save(path_to_save)
            file_to_resize = path_to_save
            resize_picture(file_to_resize)

        new_raport.img_src = self.db_path()
        db.session.commit()

    def change_report(self, id):
        raport = db.session.query(Raport, DeviceUsage, Device, TaughtSubject) \
            .select_from(Raport) \
            .join(DeviceUsage) \
            .join(Device) \
            .join(TaughtSubject) \
            .filter(Raport.id == id) \
            .order_by(desc(Raport.input_date)) \
            .all()

        device = Device.query.filter_by(name=self.device).first()
        subject = TaughtSubject.query.filter_by(subject=self.subject).first()

        for rap, deviceusage, dev, taughtsubject in raport:
            rap.description = self.description
            rap.subject = subject.id
            rap.class_date = self.date
            rap.reference = self.reference
            deviceusage.working_hours = self.working_hours
            deviceusage.deviceinfo_id = device.id
            rap.file_path = self.db_path(id)


class SummaryUsage:
    def __init__(self):
        pass

    def summary(self):
        return db.session.query(Device.name, Device.scholl_id, func.sum(DeviceUsage.working_hours)).join(
            Device).group_by(
            DeviceUsage.deviceinfo_id).all()

    def list_length(self):
        return db.session.query(Device.name, Device.scholl_id, func.sum(DeviceUsage.working_hours)).join(
            Device).group_by(
            DeviceUsage.deviceinfo_id).count()

    def count_hours(self):
        lista = self.summary()
        suma = 0
        for name, school_id, sum in lista:
            suma = suma + sum
        return suma

    def count_hours_by_user(self):
        return db.session.query(Raport.user_id, User.firstname, func.sum(DeviceUsage.working_hours)).join(User).join(
            DeviceUsage).all()

    def count_hours_by_category(self):
        lista = db.session.query(Kategoria.category_name, DeviceUsage.working_hours).select_from(
            Kategoria).join(Device).join(DeviceUsage).all()
        sum_list = []
        # tworzenie listy kategorii
        for element in lista:
            if element[0] not in sum_list:
                sum_list.append(element[0])
            else:
                pass
        # zliczanie sumy dla kategorii
        returning_list = []
        for element in sum_list:
            suma = 0
            for e in lista:
                if element == e[0]:
                    suma = suma + int(e[1])
            returning_list.append((element, suma))
        return returning_list


def delete_file_row(raportid):
    list = File.query.filter_by(raport_id=raportid).all()
    print(list)
    for element in list:
        db.session.delete(element)
    db.session.commit()
