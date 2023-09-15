from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from email_validator import validate_email, EmailNotValidError  # Import email_validator


client = MongoClient('mongodb://localhost:27017/')

if 'edvocate' not in client.list_database_names():
    db = client['edvocate']
    users = db['users']



user_data = {
                'fullname': "form.fullname.data",
                'email': "form.email.data",
                'phone': "form.phone.data",
                'aadhar_number': "form.aadhar_number.data",
                'password': "password_hash",
            }
result = users.insert_one(user_data)
if result.acknowledged:
    print("Registration successful. User ID:", result.inserted_id)
else:
    print("Registration failed. Database error.")