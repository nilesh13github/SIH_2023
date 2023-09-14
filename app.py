from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SIH'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
