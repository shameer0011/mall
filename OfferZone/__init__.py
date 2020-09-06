from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm,CSRFProtect


app=Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///offerzone.db'

db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from OfferZone import routes

