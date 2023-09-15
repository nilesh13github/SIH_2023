from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from email_validator import validate_email, EmailNotValidError
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aditya'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/edvocate'
bcrypt = Bcrypt(app)
mongo = PyMongo(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        aadhar_number = request.form['aadhar_number']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not fullname or not email or not phone or not aadhar_number or not password or not confirm_password:
            flash('Please fill out all fields.', 'danger')
        elif password != confirm_password:
            flash('Passwords do not match.', 'danger')
        elif len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password) or not any(char in '@$!%*?&_' for char in password):
            flash('Password requirements not met.', 'danger')
        else:
            try:
                validate_email(email)
                password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
                user_data = {
                    'fullname': fullname,
                    'email': email,
                    'phone': phone,
                    'aadhar_number': aadhar_number,
                    'password': password_hash,
                }
                mongo.db.users.insert_one(user_data)
                flash('Registration successful. Please log in.', 'success')
                return redirect(url_for('login'))
            except EmailNotValidError as e:
                flash('Invalid email address.', 'danger')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = mongo.db.users.find_one({'email': email})

        if user and bcrypt.check_password_hash(user['password'], password):
            flash('Login successful.', 'success')
            return render_template('login.html', user=user)
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
