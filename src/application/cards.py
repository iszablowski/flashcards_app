from flask import Blueprint, request, url_for, redirect, render_template
from flask_login import login_required, current_user
from . import db
from .models.collection_model import FlashcardsCollection
from .models.flashcard_model import Flashcard
import json

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

        


@cards.route('/edit_collection', methods=['GET', 'POST'])
@login_required
def edit_collection():
    return '1'

@cards.route('/add', methods=['GET'])
@login_required
def add_flashcard():
    return '<h3>add</h3>'


@cards.route('/remove_collection', methods=['GET'])
@login_required
def remove_collection():
    collection_to_remove_id = request.args.get('collection_id')
    collection_to_remove = FlashcardsCollection.query.filter_by(collection_id=collection_to_remove_id).first()

    if not collection_to_remove:
        return 'error-collection does not exist'

    if collection_to_remove.author_id != current_user.id:
        return 'error-this is not your collection'

    flashcards_to_remove = Flashcard.query.filter_by(collection_id=collection_to_remove_id)

    db.session.delete(collection_to_remove)
    for flashcard in flashcards_to_remove:
        db.session.delete(flashcard)

    db.session.commit()

    return redirect(url_for('flashcards.flashcards_collection'))


@cards.route('/collection/<collection_id>/train', methods=['GET'])
@login_required
def flashcards_training(collection_id):
    collection_to_train = FlashcardsCollection.query.filter_by(collection_id=collection_id).first()

    if not collection_to_train:
        return 'error-collection does not exist'

    if collection_to_train.author_id != current_user.id:
        return 'error-this is not your collection'
    
    flashcards_to_train_query = Flashcard.query.filter_by(collection_id=collection_to_train.collection_id)

    flashcards_to_train_dict = { card.card_front: card.card_description for card in flashcards_to_train_query}

    return render_template('flashcards/train.html',
                           flashcards=json.dumps(flashcards_to_train_dict),
                           user_name=current_user.name,
                           logged_in=current_user.is_authenticated,
                           collection_name=collection_to_train.collection_name)