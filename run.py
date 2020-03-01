from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_admin.contrib.peewee import ModelView
from flask_admin import Admin
from app import app
from models import *
from actions import *

admin = Admin(app, name='Locadora', template_mode='bootstrap3')

admin.add_view(ModelView(models.Tipo))
admin.add_view(ModelView(models.Usuarios))
admin.add_view(ModelView(models.Clientes))
admin.add_view(ModelView(models.Carros))
admin.add_view(ModelView(models.Alugueis))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form['cpf']

        user = Verificar.clienteExiste(cpf)

        if not user :
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html')

app.run(debug=True)