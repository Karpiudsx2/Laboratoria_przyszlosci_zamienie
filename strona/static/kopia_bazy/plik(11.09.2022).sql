--
-- File generated with SQLiteStudio v3.3.3 on niedz. wrz 11 08:40:13 2022
--
-- Text encoding used: System
--
PRAGMA
foreign_keys = off;
BEGIN
TRANSACTION;

-- Table: Classroom
CREATE TABLE "Classroom"
(
    id        INTEGER NOT NULL,
    classroom VARCHAR NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO Classroom (id, classroom)
VALUES (1, '15');
INSERT INTO Classroom (id, classroom)
VALUES (2, '19');
INSERT INTO Classroom (id, classroom)
VALUES (3, '8');
INSERT INTO Classroom (id, classroom)
VALUES (4, '23');
INSERT INTO Classroom (id, classroom)
VALUES (5, '9');
INSERT INTO Classroom (id, classroom)
VALUES (6, '9');
INSERT INTO Classroom (id, classroom)
VALUES (7, '4');
INSERT INTO Classroom (id, classroom)
VALUES (8, 'sala gimnastyczna');
INSERT INTO Classroom (id, classroom)
VALUES (9, '20');
INSERT INTO Classroom (id, classroom)
VALUES (10, '21');
INSERT INTO Classroom (id, classroom)
VALUES (11, '26');
INSERT INTO Classroom (id, classroom)
VALUES (12, '2');
INSERT INTO Classroom (id, classroom)
VALUES (13, '17');
INSERT INTO Classroom (id, classroom)
VALUES (14, '7');
INSERT INTO Classroom (id, classroom)
VALUES (15, '27');
INSERT INTO Classroom (id, classroom)
VALUES (16, '5');
INSERT INTO Classroom (id, classroom)
VALUES (17, '25');
INSERT INTO Classroom (id, classroom)
VALUES (18, '22');
INSERT INTO Classroom (id, classroom)
VALUES (19, '12');
INSERT INTO Classroom (id, classroom)
VALUES (20, '�wietlica');
INSERT INTO Classroom (id, classroom)
VALUES (21, 'inne');
INSERT INTO Classroom (id, classroom)
VALUES (22, 'sekretariat');
INSERT INTO Classroom (id, classroom)
VALUES (23, 'ksi�gowo��');
INSERT INTO Classroom (id, classroom)
VALUES (24, 'kadry');

-- Table: Device
CREATE TABLE "Device"
(
    id           INTEGER      NOT NULL,
    scholl_id    VARCHAR(3)   NOT NULL,
    kategoria_id VARCHAR(50),
    name         VARCHAR(150) NOT NULL,
    description  VARCHAR(500),
    PRIMARY KEY (id),
    FOREIGN KEY (kategoria_id) REFERENCES "Kategoria" (id)
);
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (1, 'S1', '1', 'Drukarka 3d MakerBot SKETCH', 'Drukarka 3D wraz z akcesoriami oraz szkoleniami z obs�ugi.



Specyfikacja techniczna:







��czno�� Wi-Fi



Zdalny podgl�d wydruku � wbudowana kamera



Obszar roboczy min: 15 x 15 x 15 cm



Natywna obs�uga kilku rodzaj�w plik�w wej�ciowych: STL, SolidWorks, Solid Edge, Catia, Unigraphics



Kompatybilny slicer � dedykowane, intuicyjne oprogramowanie



Gwarancja: Przynajmniej 24 miesi�ce



Autoryzowany serwis na terenie Polski



Serwis i wsparcie techniczne w j�zyku polskim



Instrukcja obs�ugi w j�zyku polskim











Akcesoria do drukarki



 � Biodegradowalny filament PLA przynajmniej 5 kg



 � St� roboczy, w tym zestaw narz�dzi: szpachelka, c��ki do usuwania podp�r oraz inne akcesoria



 � Baza modeli 3D



 � Szkolenie startowe dla nauczycieli prowadzone w formie zdalnej lub stacjonarnej







   � Mo�liwo�� pod��czenia poprzez urz�dzenia mobilne



 � Instrukcja obs�ugi w j�zyku polskim');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (2, 'S2', '1', 'Drukarka 3D MakerBot Method X', 'Drukarka 3D wraz z akcesoriami oraz szkoleniami z obs�ugi.



Specyfikacja techniczna:



��czno�� Wi-Fi



Minimalna wysoko�� warstwy: 0,02 mm



Zdalny podgl�d wydruku � wbudowana kamera



Obszar roboczy min: 19 x 19 x 19 cm



Natywna obs�uga kilku rodzaj�w plik�w wej�ciowych: STL, SolidWorks, Solid Edge, Catia, Unigraphics



Kompatybilny slicer � dedykowane, intuicyjne oprogramowanie



Gwarancja: Przynajmniej 24 miesi�ce



Autoryzowany serwis na terenie Polski



Serwis i wsparcie techniczne w j�zyku polskim



Instrukcja obs�ugi w j�zyku polskim







Akcesoria do drukarki



 � Biodegradowalny filament PLA przynajmniej 5 kg



 � St� roboczy, w tym zestaw narz�dzi: szpachelka, c��ki do usuwania podp�r oraz inne akcesoria



 � Baza modeli 3D



 � Szkolenie startowe dla nauczycieli prowadzone w formie zdalnej lub stacjonarnej



� Mo�liwo�� pod��czenia poprzez urz�dzenia mobilne



 � Instrukcja obs�ugi w j�zyku polskim');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (3, 'S3', '6', 'Filament biodegradowalny PLA', 'Dedykowany filament do drukarki 3d w r�nych kolorach



Min: 38kg 



Rodzaj filamentu: PLA');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (4, 'S4', '4', 'Skaner 3d', 'Specyfikacja techniczna:







Dok�adno�� skanowania: 0.1mm



Rozmiar skanowanych przedmiot�w do 700 x 700 x 700mm



Ud�wig stolika: przynajmniej 4kg



Obs�uga plik�w CAD: w tym OBJ,STL,ASC,PLY');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (5, 'S5', '1', 'Zestawy do programowania mikrokontroler�w i nauki elektroniki', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (6, 'S6', '4', 'Zestaw edukacyjny z Raspberry Pi 4B', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (7, 'S7', '1', 'Mikroport', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (8, 'S8', '1', 'Stacja lutownicza', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (9, 'S9', '1', 'Stacja lutownicza', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (10, 'S10', '1', 'Uchwyt uniwersalny Gimbal', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (11, 'S11', '1', 'Mikrofon biurkowy z podstawk�', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (12, 'S12', '1', 'Mikrofon kierunkowy nakamerowy', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (13, 'S13', '1', 'Statyw', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (14, 'S14', '1', 'Zestaw o�wietlenia ci�g�ego', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (15, 'S15', '3', 'Suwmiarka', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (16, 'S16', '3', 'N� z ostrzem �amanym', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (17, 'S17', '3', 'Waga laboratoryjna szalkowa', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (18, 'S18', '8', '�awa optyczna z pe�nym wyposa�eniem', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (19, 'S19', '2', 'Skrzynka narz�dziowa', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (20, 'S20', '3', 'Miernik temperatury Pirometr', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (21, 'S21', '3', 'Obcinaczki boczne 110mm', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (22, 'S22', '3', 'Zestaw wkr�tak�w i bit�w z magnetyzerem', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (23, 'S23', '4', 'Robot edukacyjny do samodzielnego z�o�enia', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (24, 'S24', '4', 'Robot edukacyjny do samodzielnego z�o�enia', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (25, 'S25', '4', 'D�ugopis 3d', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (26, 'S26', '4', 'Wizualizer', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (27, 'S27', '5', 'Maszyna do szycia', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (28, 'S28', '5', 'Maszyna do szycia dla dzieci', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (29, 'S29', '8', 'Zestaw do monta�u podstawowych obwod�w elektrycznych', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (30, 'S30', '8', 'Komplet do monta�u obwod�w elektrycznych z silniczkiem', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (31, 'S31', '7', 'G�o�niki bezprzewodowe', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (32, 'S32', '8', 'Plansza podstawowe wzory fizyczne', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (33, 'S33', '8', 'Plansza ruch prostolinijny', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (34, 'S34', '8', 'Jednostki miar', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (35, 'S35', '8', 'Maszyny proste -  plansza', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (36, 'S36', '8', 'Zasady dynamiki', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (37, 'S37', '2', 'St� warsztatowy z wyposa�eniem', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (38, 'S38', '7', 'Green screen mobilny w obudowie', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (39, 'S39', '1', 'Filamenty do d�ugopisu 3D - 50 m', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (40, 'S40', '1', 'Filamenty do d�ugopisu Banach 3D - 200 m', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (41, 'S41', '5', 'Urz�dzenie multifunkcyjne�', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (42, 'S42', '5', 'Blender r�czny', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (43, 'S43', '7', 'Przeno�ny zestaw nag�o�nieniowy', '');
INSERT INTO Device (id, scholl_id, kategoria_id, name, description)
VALUES (44, 'S44', '3', 'Kombinerki', '');

-- Table: DeviceUsage
CREATE TABLE "DeviceUsage"
(
    id            INTEGER NOT NULL,
    deviceinfo_id INTEGER,
    working_hours FLOAT   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (deviceinfo_id) REFERENCES "Device" (id) ON DELETE CASCADE
);
INSERT INTO DeviceUsage (id, deviceinfo_id, working_hours)
VALUES (1, 12, 0.75);
INSERT INTO DeviceUsage (id, deviceinfo_id, working_hours)
VALUES (2, 3, 1.0);
INSERT INTO DeviceUsage (id, deviceinfo_id, working_hours)
VALUES (3, 14, 10.0);
INSERT INTO DeviceUsage (id, deviceinfo_id, working_hours)
VALUES (4, 1, 1.0);
INSERT INTO DeviceUsage (id, deviceinfo_id, working_hours)
VALUES (5, 13, 2.25);
INSERT INTO DeviceUsage (id, deviceinfo_id, working_hours)
VALUES (6, 1, 4.75);
INSERT INTO DeviceUsage (id, deviceinfo_id, working_hours)
VALUES (7, 44, 7.0);

-- Table: Kategoria
CREATE TABLE "Kategoria"
(
    id            INTEGER     NOT NULL,
    category_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO Kategoria (id, category_name)
VALUES (1, 'wyposa�enie podstawowe');
INSERT INTO Kategoria (id, category_name)
VALUES (2, 'wyposa�enie stanowisk');
INSERT INTO Kategoria (id, category_name)
VALUES (3, 'narz�dzia');
INSERT INTO Kategoria (id, category_name)
VALUES (4, 'robotyka');
INSERT INTO Kategoria (id, category_name)
VALUES (5, 'AGD');
INSERT INTO Kategoria (id, category_name)
VALUES (6, 'materia�y eksploatacyjne');
INSERT INTO Kategoria (id, category_name)
VALUES (7, 'audio-wideo');
INSERT INTO Kategoria (id, category_name)
VALUES (8, 'pomoce projektowe');
INSERT INTO Kategoria (id, category_name)
VALUES (9, 'BHP');

-- Table: Malfunctinon
CREATE TABLE "Malfunctinon"
(
    id          INTEGER NOT NULL,
    user_id     INTEGER,
    description INTEGER NOT NULL,
    take_care   BOOLEAN,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES "User" (id)
);

-- Table: Raport
CREATE TABLE "Raport"
(
    id             INTEGER       NOT NULL,
    user_id        INTEGER,
    deviceusage_id INTEGER,
    subject        INTEGER,
    input_date     DATETIME,
    class_date     DATETIME      NOT NULL,
    reference      VARCHAR(500)  NOT NULL,
    description    VARCHAR(5000) NOT NULL,
    file_path      VARCHAR(200),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES "User" (id),
    FOREIGN KEY (deviceusage_id) REFERENCES "DeviceUsage" (id),
    FOREIGN KEY (subject) REFERENCES "TaughtSubject" (id)
);
INSERT INTO Raport (id, user_id, deviceusage_id, subject, input_date, class_date, reference, description, file_path)
VALUES (1, 1, 1, 12, '2022-08-23 21:53:56', '2022-08-06 00:00:00.000000', 'Figury 3d', 'sdasda',
        'C:\Users\KaRpiU\PycharmProjects\Laboratoria_przyszlo�ci\strona\static\RaportPhotos\Raport1');
INSERT INTO Raport (id, user_id, deviceusage_id, subject, input_date, class_date, reference, description, file_path)
VALUES (2, 1, 2, 12, '2022-08-29 11:09:43', '2022-08-19 00:00:00.000000', 'Figury 3d',
        'Urz�dzenie pos�u�y�o do stworzenia stwoka potworka na lekcje matematyki',
        'C:\Users\KaRpiU\PycharmProjects\Laboratoria_przyszlo�ci\strona\static\RaportPhotos\Raport2');
INSERT INTO Raport (id, user_id, deviceusage_id, subject, input_date, class_date, reference, description, file_path)
VALUES (3, 3, 3, 13, '2022-09-04 12:46:39', '2022-09-22 00:00:00.000000', 'kkkkk', 'taaaa',
        'C:\Users\KaRpiU\PycharmProjects\Laboratoria_przyszlo�ci\strona\static\RaportPhotos\Raport3');
INSERT INTO Raport (id, user_id, deviceusage_id, subject, input_date, class_date, reference, description, file_path)
VALUES (4, 4, 4, 12, '2022-09-04 15:16:16', '2022-10-02 00:00:00.000000', 'Figury przestrzenne',
        'Sprz�t zosta� u�yty do wykonania modeli 3d.', 'raportphotos/Raport4/wallhaven-4gj9xq.jpg');
INSERT INTO Raport (id, user_id, deviceusage_id, subject, input_date, class_date, reference, description, file_path)
VALUES (5, 4, 5, 8, '2022-09-04 15:27:39', '2022-09-22 00:00:00.000000', 'sasdasdasd', 'To m�j nowy opis',
        'raportphotos/Raport5/wallhaven-5333.jpg');
INSERT INTO Raport (id, user_id, deviceusage_id, subject, input_date, class_date, reference, description, file_path)
VALUES (6, 1, 6, 4, '2022-09-04 17:03:16', '2022-09-08 00:00:00.000000', 'sdfsdfsdfs', 'dfsdfd',
        'raportphotos/Raport6/wallhaven-013rgw.jpg');
INSERT INTO Raport (id, user_id, deviceusage_id, subject, input_date, class_date, reference, description, file_path)
VALUES (7, 1, 7, 2, '2022-09-04 17:49:06', '2022-09-24 00:00:00.000000', 'asdasdasdsadasdasdasdasdasdasdasdasd',
        'Zmieniono',
        '[''raportphotos/Raport7/wallhaven-8oxmr2.jpg'', ''raportphotos/Raport7/wallhaven-013rgw.jpg'', ''raportphotos/Raport7/wallhaven-5333.jpg'']');

-- Table: TaughtSubject
CREATE TABLE "TaughtSubject"
(
    id      INTEGER     NOT NULL,
    subject VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO TaughtSubject (id, subject)
VALUES (1, 'biologia');
INSERT INTO TaughtSubject (id, subject)
VALUES (2, 'chemia');
INSERT INTO TaughtSubject (id, subject)
VALUES (3, 'edukacja dla bezpiecze�stwa');
INSERT INTO TaughtSubject (id, subject)
VALUES (4, 'edukacja wczesnoszkolna');
INSERT INTO TaughtSubject (id, subject)
VALUES (5, 'fizyka');
INSERT INTO TaughtSubject (id, subject)
VALUES (6, 'geografia');
INSERT INTO TaughtSubject (id, subject)
VALUES (7, 'historia');
INSERT INTO TaughtSubject (id, subject)
VALUES (8, 'informatyka');
INSERT INTO TaughtSubject (id, subject)
VALUES (9, 'j�zyk angielski');
INSERT INTO TaughtSubject (id, subject)
VALUES (10, 'drugi j�zyk nowo�ytny');
INSERT INTO TaughtSubject (id, subject)
VALUES (11, 'j�zyk polski');
INSERT INTO TaughtSubject (id, subject)
VALUES (12, 'matematyka');
INSERT INTO TaughtSubject (id, subject)
VALUES (13, 'muzyka');
INSERT INTO TaughtSubject (id, subject)
VALUES (14, 'plastyka');
INSERT INTO TaughtSubject (id, subject)
VALUES (15, 'przyroda');
INSERT INTO TaughtSubject (id, subject)
VALUES (16, 'technika');
INSERT INTO TaughtSubject (id, subject)
VALUES (17, 'technika');
INSERT INTO TaughtSubject (id, subject)
VALUES (18, 'wiedza o spo�ecz�stwie');
INSERT INTO TaughtSubject (id, subject)
VALUES (19, 'wychowanie fizyczne');
INSERT INTO TaughtSubject (id, subject)
VALUES (20, 'religia');
INSERT INTO TaughtSubject (id, subject)
VALUES (21, 'wychowanie do �ycia w rodzinie');
INSERT INTO TaughtSubject (id, subject)
VALUES (22, 'zaj�cia z wychowawc�');
INSERT INTO TaughtSubject (id, subject)
VALUES (23, 'zaj�cia wyr�wnawcze');
INSERT INTO TaughtSubject (id, subject)
VALUES (24, 'ko�a zainteresowa�');
INSERT INTO TaughtSubject (id, subject)
VALUES (25, 'terapia pedagogiczna');
INSERT INTO TaughtSubject (id, subject)
VALUES (26, 'zaj�cia korekcyjno-kompensacyjna');
INSERT INTO TaughtSubject (id, subject)
VALUES (27, 'inne');

-- Table: User
CREATE TABLE "User"
(
    id          INTEGER      NOT NULL,
    email       VARCHAR(150),
    subject1_id INTEGER      NOT NULL,
    subject2_id INTEGER,
    subject3_id INTEGER,
    password    VARCHAR(150) NOT NULL,
    firstname   VARCHAR(150) NOT NULL,
    lastname    VARCHAR(150) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (email),
    FOREIGN KEY (subject1_id) REFERENCES "TaughtSubject" (id),
    FOREIGN KEY (subject2_id) REFERENCES "TaughtSubject" (id),
    FOREIGN KEY (subject3_id) REFERENCES "TaughtSubject" (id)
);
INSERT INTO User (id, email, subject1_id, subject2_id, subject3_id, password, firstname, lastname)
VALUES (1, 'karpiniakpiotr@gmail.com', 12, NULL, NULL,
        'pbkdf2:sha256:260000$ZWFkBBnqxsQHsqpH$d61d792a6f0a3eb22110911be5f8fee8a0dace85421b65c3bec87e8b466bf1ef',
        'Wis�aw', 'Karpiniak');
INSERT INTO User (id, email, subject1_id, subject2_id, subject3_id, password, firstname, lastname)
VALUES (2, 'KowalczykRyszard@protonmail.com', 9, NULL, NULL,
        'pbkdf2:sha256:260000$YuCtO8OC4BQUV8h0$be6fea952a7a7093fe4feab1ffa96954edf492eb5dc9bd59def0b936a7a05145',
        'Piotr', 'Karpiniak');
INSERT INTO User (id, email, subject1_id, subject2_id, subject3_id, password, firstname, lastname)
VALUES (3, 'zdzislaw.sienkiwicz@spsekocin.com.pl', 2, NULL, NULL,
        'pbkdf2:sha256:260000$w1VlcFVMmBrwWKKH$a58aa40efba164537fb18d1b1fdce8487b96f9b85eb3e1391bc9185a868c965c',
        'Zdzis�aw', 'Sienkiewicz');
INSERT INTO User (id, email, subject1_id, subject2_id, subject3_id, password, firstname, lastname)
VALUES (4, 'kapriowygaj@gmail.com', 8, NULL, NULL,
        'pbkdf2:sha256:260000$v1SOPSSDMxbufYa6$b01fd7a36f6b216514eb86afd26894cadffe65a7c79622f143614da28de75b57',
        'Piotr', 'Sienkiewicz');

COMMIT TRANSACTION;
PRAGMA
foreign_keys = on;
