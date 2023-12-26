from flask import Blueprint, request, url_for, redirect, render_template

home = Blueprint('home', __name__)

@home.route('/')
def home_page():
    return '<h3>Home page<h3>'
