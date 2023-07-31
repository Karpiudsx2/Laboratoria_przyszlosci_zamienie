INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('table', 'TaughtSubject', 'TaughtSubject', 2, 'CREATE TABLE "TaughtSubject" (
	id INTEGER NOT NULL, 
	subject VARCHAR(30) NOT NULL, 
	PRIMARY KEY (id)
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('table', 'Kategoria', 'Kategoria', 3, 'CREATE TABLE "Kategoria" (
	id INTEGER NOT NULL, 
	category_name VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id)
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('table', 'Classroom', 'Classroom', 4, 'CREATE TABLE "Classroom" (
	id INTEGER NOT NULL, 
	classroom VARCHAR NOT NULL, 
	PRIMARY KEY (id)
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('table', 'User', 'User', 5, 'CREATE TABLE "User" (
	id INTEGER NOT NULL, 
	email VARCHAR(150), 
	subject1_id INTEGER NOT NULL, 
	subject2_id INTEGER, 
	subject3_id INTEGER, 
	password VARCHAR(150) NOT NULL, 
	firstname VARCHAR(150) NOT NULL, 
	lastname VARCHAR(150) NOT NULL, 
	is_admin BOOLEAN, 
	is_managment BOOLEAN, 
	reset_password VARCHAR(300), 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	FOREIGN KEY(subject1_id) REFERENCES "TaughtSubject" (id), 
	FOREIGN KEY(subject2_id) REFERENCES "TaughtSubject" (id), 
	FOREIGN KEY(subject3_id) REFERENCES "TaughtSubject" (id)
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('index', 'sqlite_autoindex_User_1', 'User', 6, null);
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('table', 'Device', 'Device', 7, 'CREATE TABLE "Device" (
	id INTEGER NOT NULL, 
	scholl_id VARCHAR(3) NOT NULL, 
	kategoria_id VARCHAR(50), 
	name VARCHAR(150) NOT NULL, 
	description VARCHAR(500), 
	photo VARCHAR(500), 
	PRIMARY KEY (id), 
	FOREIGN KEY(kategoria_id) REFERENCES "Kategoria" (id)
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('table', 'DeviceUsage', 'DeviceUsage', 8, 'CREATE TABLE "DeviceUsage" (
	id INTEGER NOT NULL, 
	deviceinfo_id INTEGER, 
	working_hours FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(deviceinfo_id) REFERENCES "Device" (id)
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('table', 'Malfunctinon', 'Malfunctinon', 9, 'CREATE TABLE "Malfunctinon" (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	description INTEGER NOT NULL, 
	take_care BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES "User" (id)
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('table', 'Raport', 'Raport', 10, 'CREATE TABLE "Raport" (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	deviceusage_id INTEGER, 
	subject INTEGER, 
	input_date DATETIME, 
	class_date DATETIME NOT NULL, 
	reference VARCHAR(500) NOT NULL, 
	description VARCHAR(5000) NOT NULL, 
	uwagi VARCHAR(1000), 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES "User" (id), 
	FOREIGN KEY(deviceusage_id) REFERENCES "DeviceUsage" (id) ON DELETE CASCADE, 
	FOREIGN KEY(subject) REFERENCES "TaughtSubject" (id)
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql)
VALUES ('table', 'File', 'File', 11, 'CREATE TABLE "File" (
	id INTEGER NOT NULL, 
	typ VARCHAR NOT NULL, 
	filename VARCHAR NOT NULL, 
	raport_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(raport_id) REFERENCES "Raport" (id)
)');