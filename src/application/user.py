from flask import Blueprint, request, url_for, redirect, render_template
from flask_login import login_required, current_user

user = Blueprint('user', __name__, url_prefix='/profile')

@user.route('/', methods=['GET'])
@login_required
def user_page():
    return render_template('base.html', user_name=current_user.name, logged_in=current_user.is_authenticated)

@user.route('/settings', methods=['GET', 'POST'])
def user_settings():
    return '<h3>settings</h3>'

@user.route('/collection', methods=['GET'])
def user_collection():
    return '<h3>collection</h3>'
