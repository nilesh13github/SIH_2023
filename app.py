from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
<<<<<<< HEAD

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
=======
from flask_wtf import FlaskForm

>>>>>>> 1dd4fdc9c23630898d96df86bfb7b6cc198f97ee
