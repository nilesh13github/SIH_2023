from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from email_validator import validate_email, EmailNotValidError  # Import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aditya'
bcrypt = Bcrypt(app)
client = MongoClient('mongodb://localhost:27017/')
db = client['edvocate']
users = db['users']

class RegistrationForm(FlaskForm):
    fullname = StringField('Full Name', validators=[validators.InputRequired()])
    email = StringField('Email', validators=[
        validators.InputRequired(),
        validators.Email(message='Invalid email address'),  # Basic email validation
    ])
    phone = StringField('Phone Number', validators=[validators.InputRequired()])
    aadhar_number = StringField('Aadhar Number', validators=[validators.InputRequired()])
    password = PasswordField('Password', validators=[
        validators.InputRequired(),
        validators.Length(min=8),
        validators.EqualTo('confirm_password', message='Passwords must match'),
        validators.Regexp(
            '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&])',
            message='Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character'
        )
    ])
    confirm_password = PasswordField('Re-enter Password', validators=[validators.InputRequired()])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            validate_email(form.email.data)  # Validate email using email_validator
            password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user_data = {
                'fullname': form.fullname.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'aadhar_number': form.aadhar_number.data,
                'password': password_hash,
            }
            users.insert_one(user_data)
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        except EmailNotValidError as e:
            flash('Invalid email address.', 'danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = users.find_one({'email': email, 'password': password})
        if user:
            flash('Login successful.', 'success')
            return render_template('login.html', user=user)
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

