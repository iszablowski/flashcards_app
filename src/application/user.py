from flask import Blueprint, request, url_for, redirect, render_template

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<user_name>', methods=['GET'])
def user_page(user_name):
    return f'<h3>{user_name}</h3>'
