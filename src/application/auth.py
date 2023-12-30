from flask import Blueprint, request, url_for, redirect, render_template, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models.user_model import User
from . import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home_page'))

    if request.method == 'GET':
        return render_template('auth/login.html')
    
    elif request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(name=username).first()

        if not user:
            flash('User does not exist.')
            return redirect(url_for('auth.login'))
        
        if not check_password_hash(user.password, password):
            flash('Wrong password.')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        return redirect(url_for('user.user_page'))
        
@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('home.home_page'))

    if request.method == 'GET':
        return render_template('auth/signup.html')

    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirmation = request.form.get('password-confirmation')

        user = User.query.filter_by(name=username).first()

        if user:
            flash('User already exists.')
            return redirect(url_for('auth.sign_up'))
        
        if password != password_confirmation:
            flash('Passwords are not the same.')
            return redirect(url_for('auth.sign_up'))
        
        new_user = User(name=username, password=generate_password_hash(password))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home_page'))

