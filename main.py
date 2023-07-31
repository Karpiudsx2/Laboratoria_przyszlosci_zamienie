# Jedyną rolą aplikacji main.py jest uworzenie aplikacji Flask
from flask import request

from strona import app
from strona.functions import *

app.jinja_env.globals.update(getting_taught_subjects=getting_taught_subjects)

if __name__ == '__main__':
    app.run(debug=True)
