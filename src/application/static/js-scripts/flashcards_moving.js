const card_text = document.querySelector('#card-value');
const button_previous = document.querySelector('#go-previous');
const button_next = document.querySelector('#go-next');
const card = document.querySelector('.train-card');

let front; let back;
let current_flashcard_index = 0;
const max_flashcard_index = Object.keys(flashcards).length-1;

function get_current_flashcard(index) {
    let front = Object.keys(flashcards)[index];
    return [front, flashcards[front]];
}

function init_training() {
    [front, back] = get_current_flashcard(current_flashcard_index);
    card_text.value = 'front';
    card_text.innerHTML = front;
}

function set_flashcard_side() {
    
    if (card_text.value === 'front') {
        card_text.innerHTML = back;
        card_text.value = 'back';
    } else if (card_text.value === 'back') {
        card_text.innerHTML = front;
        card_text.value = 'front';
    }
}

function set_flashcard_content() {
    card_text.value = 'front';
    [front, back] = get_current_flashcard(current_flashcard_index);
    card_text.innerHTML = front;
}

function next_card() {
    if (current_flashcard_index < max_flashcard_index) {
        current_flashcard_index++;
        set_flashcard_content();
    }
}

function previous_card() {
    if (current_flashcard_index > 0) {
        current_flashcard_index--;
        set_flashcard_content();
    }
}

card.addEventListener('click', set_flashcard_side);
button_next.addEventListener('click', next_card);
button_previous.addEventListener('click', previous_card);


init_training();