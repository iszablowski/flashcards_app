class Flashcard:

    def __init__(self, front: str, description: str, priority: int):
        self._front = front
        self._description = description
        self._priority = priority

    @property
    def get_front(self) -> str:
        return self._front
    
    @property
    def get_description(self) -> str:
        return self._description
    
    @property
    def get_priority(self) -> int:
        return self._priority
    
    def set_front(self, new_front: str):
        self._front = new_front

    def set_description(self, new_description: str):
        self._description = new_description

    def __lt__(self, second_flashcard) -> bool:
        return self._front.lower() < second_flashcard.get_front.lower()
    
    def __str__(self):
        return self._front + ' : ' + self._description