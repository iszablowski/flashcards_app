from flashcard_class import Flashcard

class FlashcardsCollection:
    
    def __init__(self, init_collection = []):
        self._collection = init_collection
    
    @property
    def get_collection(self):
        return self._collection
    
    def add_flashcard(self, flashcard: Flashcard):
        self._collection.append(flashcard)

    def sort(self):
        self._collection.sort()

    def remove_flashcard(self, card_index: str):
        self._collection.pop(card_index)

    def __str__(self):
        description = ''
        for card in self._collection:
            description += str(card) + '\n'
        return description
