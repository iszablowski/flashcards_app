from flask import Blueprint, request, url_for, redirect, render_template
from flask_login import current_user

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def home_page():
    if current_user.is_authenticated:
        return render_template('base.html', logged_in=current_user.is_authenticated, user_name=current_user.name)
    else:
        return render_template('base.html', logged_in=current_user.is_authenticated)
