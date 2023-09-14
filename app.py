from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
