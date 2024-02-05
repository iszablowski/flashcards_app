from flask import Blueprint, request, url_for, redirect, render_template, flash
from flask_login import login_required, current_user
from .models.user_model import User
from . import db

user = Blueprint('user', __name__, url_prefix='/profile')

@user.route('/', methods=['GET'])
@login_required
def user_page():
    return render_template('user/profile.html', user_name=current_user.name, logged_in=current_user.is_authenticated)

@user.route('/', methods=['POST'])
@login_required
def set_username():
    new_user_name = request.form.get('new-username')

    user = User.query.filter_by(name=current_user.name).first()

    user_with_new_name = User.query.filter_by(name=new_user_name).first()

    if not user_with_new_name:
        user.name = new_user_name
        db.session.add(user)
        db.session.commit()
        flash('Name has successfully changed.')
    else:
        flash('Name is already taken.')

    return redirect(url_for('user.user_page'))
