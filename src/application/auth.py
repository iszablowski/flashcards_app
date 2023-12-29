from flask import Blueprint, request, url_for, redirect, render_template

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('auth/signin.html')
    

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('auth/signup.html')
    
@auth.route('/logout', methods=['GET'])
def logout():
    return '<h3>Logout</h3>'

