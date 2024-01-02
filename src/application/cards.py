from flask import Blueprint, request, url_for, redirect, render_template
from flask_login import login_required, current_user
from . import db
from .models.collection_model import FlashcardsCollection
from .models.flashcard_model import Flashcard

cards = Blueprint('flashcards', __name__, url_prefix='/flashcards')


@cards.route('/collection/<collection_id>', methods=['GET'])
@login_required
def flashcards(collection_id):

    collection = FlashcardsCollection.query.filter_by(collection_id=collection_id).first()

    if not collection:
        return 'error-collection does not exist'
    
    collection_author_id = collection.author_id

    if collection_author_id != current_user.id:
        return 'error-this is not your collection'
    
    flashcards_collection = Flashcard.query.filter_by(collection_id=collection_id)

    return render_template('/flashcards/flashcards.html',
                           user_name=current_user.name,
                           logged_in=current_user.is_authenticated,
                           collection=flashcards_collection,
                           collection_name=collection.collection_name)

@cards.route('/collection', methods=['GET'])
@login_required
def flashcards_collection():

    user_collections = FlashcardsCollection.query.filter_by(author_id=current_user.id)

    return render_template('flashcards/flashcards_collection.html',
                           user_name=current_user.name,
                           logged_in=current_user.is_authenticated,
                           collections=user_collections)

@cards.route('/create_collection', methods=['GET', 'POST'])
@login_required
def create_collection():
    if request.method == 'GET':
        return render_template('flashcards/create_collection.html',
                               user_name=current_user.name,
                               logged_in=current_user.is_authenticated)
    
    if request.method == 'POST':

        collection_name = request.form.get('collection-name')
        card_fronts = request.form.getlist('card-front')
        card_descriptions = request.form.getlist('card-description')

        new_collection = FlashcardsCollection(author_id=current_user.id, collection_name=collection_name)
        db.session.add(new_collection)

        db.session.commit()

        for front, description in zip(card_fronts, card_descriptions):
            new_flashcard = Flashcard(collection_id=new_collection.collection_id, card_front=front, card_description=description)
            db.session.add(new_flashcard)
        
        db.session.commit()

        return redirect(url_for('flashcards.flashcards', collection_id=new_collection.collection_id))

        

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