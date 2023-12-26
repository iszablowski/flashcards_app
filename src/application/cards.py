from flask import Blueprint, request, url_for, redirect, render_template

cards = Blueprint('cards', __name__, url_prefix='/cards')