from flask import Blueprint, request, url_for, redirect, render_template
from flask_login import login_required, current_user

cards = Blueprint('flashcards', __name__, url_prefix='/flashcards')


@login_required
@cards.route('/', methods=['GET'])
def flashcards():
    return '<h3>flashcards<h3>'

@cards.route('/create_collection', methods=['GET', 'POST'])
@login_required
def create_collection():
    return render_template('flashcards/create_collection.html', user_name=current_user.name, logged_in=current_user.is_authenticated)

@login_required
@cards.route('/edit_collection', methods=['GET', 'POST'])
def edit_collection():
    return 1

@login_required
@cards.route('/add', methods=['GET'])
def add_flashcard():
    return '<h3>add</h3>'

@login_required
@cards.route('/remove', methods=['GET'])
def remove_flashcard():
    return '<h3>rmeove</h3>'

@login_required
@cards.route('/training', methods=['GET'])
def flashcards_training():
    return '<h3>training</h3>'