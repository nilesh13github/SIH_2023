from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["edvocatedb"]
mycol=mydb["client_users"]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SIH'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)



