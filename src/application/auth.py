from flask import Blueprint, request, url_for, redirect, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from .models.user_model import User
from . import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('auth/signup.html')

    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirmation = request.form.get('password-confirmation')

        user = User.query.filter_by(name=username).first()

        if user or password != password_confirmation:
            return redirect(url_for('auth.sign_up'))
        
        new_user = User(name=username, password=generate_password_hash(password))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
@auth.route('/logout', methods=['GET'])
def logout():
    return '<h3>Logout</h3>'

