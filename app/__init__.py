from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '696867'
app.config['FLASK_ADMIN_SWATCH'] = 'journal'


login_manager = LoginManager(app)
