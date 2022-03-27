# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:10:48 2022

@author: ivan.lorenzo

f = open("listado_cursos.txt")
print(f)
f.close()
help(print)
import os
os. getcwd()
os.chdir('C:\\Users\\ivan.lorenzo\\Downloads\\prgs\\nuevas\\Udemy Complete Python Developer In 2020 Zero To Mastery\\0_ejercicios')

with open('my_data.csv', 'r') as infile, open('data_out.csv', 'w') as outfile:
    for line in infile:
        outfile.write(line)

import csv
with open('some.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

python crear entorno virtual
el primer "venv" es la instrucción, y el segundo, el nombre del entorno virtual que podría ser "patata"
py -3 -m venv venv
python activar entorno virtual, que es diferente para cmd y para powershell
cmd
nombre_entorno_virtual\Scripts\activate.bat
cmd
nombre_entorno_virtual\Scripts\deactivate.bat
powershell
nombre_entorno_virtual\Scripts\Activate.ps1

Antes de ejecutar la aplicación, en cmc:
    set FLASK_APP=server.py
Pero para ver los cambios sin tener que estar reiniciando el servidor
constantemente, es mejor:
    set FLASK_ENV=development
Seguidamente:
    flask run
Para parar el servidor:
    Ctrl+C
"""
# 20220327 - Comentario para hacer pruebas en git-hub
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(app)
print(__name__)


@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)


# @app.route('/')
# def hello_world():
#     return 'Hola Perola'


@app.route('/')
def main_home():
    return render_template("index.html")

# esta fue mi solución

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == "POST":
#         data = request.form.to_dict()
#         print(f"La información enviada con el formulario es {data}")
#         with open("../database.txt", "a") as file:
#             record = "\n" + ",".join((data.get("email", "no existe"), data.get(
#                 "subject", "no existe"), data.get("message", "no existe")))
#             file.write(record)

#         return redirect("/thankyou.html")
#     return "Fallo en el método"

# esta es la solución del instructor, mejorada por mí, a la hora de obtener
# los valores del diccionario


def write_to_file(data):
    email = data.get("email", "no existe")
    subject = data.get("subject", "no existe")
    message = data.get("message", "no existe")
    with open("../database.txt", "a") as f:
        f.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    email = data.get("email", "no existe")
    subject = data.get("subject", "no existe")
    message = data.get("message", "no existe")
    with open("../database.csv", newline='', mode="a") as fcsv:
        # email = data.get("email", "no existe")
        # subject = data.get("subject", "no existe")
        # message = data.get("message", "no existe")
        csv_writer = csv.writer(
            fcsv, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(f"La información enviada con el formulario es {data}")
        # write_to_file(data)
        write_to_csv(data)
        return redirect("/thankyou.html")
    return "Fallo en el método"


# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template("index.html", name=username)

# @app.route('/')
# def my_home():
#     return render_template("index.html")


# @app.route('/index.html')
# def my_home_nav_bar():
#     return render_template("index.html")


# @app.route('/works.html')
# def my_works_nav_bar():
#     return render_template("works.html")


# @app.route('/about.html')
# def my_about_nav_bar():
#     return render_template("about.html")


# @app.route('/components.html')
# def my_components_nav_bar():
#     return render_template("components.html")


# @app.route('/contact.html')
# def my_contact_nav_bar():
#     return render_template("contact.html")


# @app.route('/work.html')
# def my_work_nav_bar():
#     return render_template("work.html")
