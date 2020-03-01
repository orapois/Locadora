from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
import models 

app = Flask(__name__)

app.config['SECRET_KEY'] = '696867'
app.config['FLASK_ADMIN_SWATCH'] = 'journal'

admin = Admin(app, name='Locadora', template_mode='bootstrap3')

admin.add_view(ModelView(models.Tipo))
@app.route('/')

def index():
    return '<a href="/admin/">admin</a>'

if __name__ == '__main__':
    app.run(debug=True)