from flask import Blueprint, request, url_for, redirect, render_template

cards = Blueprint('flashcards', __name__, url_prefix='/flashcards')


@cards.route('/', methods=['GET'])
def flashcards():
    return '<h3>flashcards<h3>'

@cards.route('/add', methods=['GET'])
def add_flashcard():
    return '<h3>add</h3>'

@cards.route('/remove', methods=['GET'])
def remove_flashcard():
    return '<h3>rmeove</h3>'

@cards.route('/training', methods=['GET'])
def flashcards_training():
    return '<h3>training</h3>'