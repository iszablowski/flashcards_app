from flask import Blueprint, request, url_for, redirect, render_template

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def home_page():
    return render_template('base.html')
