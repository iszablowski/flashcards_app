const card_text = document.querySelector('#card-value');
const button_previous = document.querySelector('#go-previous');
const button_next = document.querySelector('#go-next');
const card = document.querySelector('.train-card');
const flashcard_number = document.querySelector('#flashcard-number');

let front; let back;
let current_flashcard_index = 0;
const max_flashcard_index = flashcards.length-1;

function get_current_flashcard(index) {
    let front = flashcards[index][0];
    let back = flashcards[index][1];
    return [front, back];
}

function update_flashcard_number() {
    flashcard_number.innerHTML = `${current_flashcard_index+1} / ${max_flashcard_index+1}`;
}

function init_training() {
    [front, back] = get_current_flashcard(current_flashcard_index);
    card_text.className = 'front';
    card_text.innerHTML = front;
    update_flashcard_number();
}

function set_flashcard_side() {
    
    if (card_text.className === 'front') {
        card_text.innerHTML = back;
        card_text.className = 'back';
    } else if (card_text.className === 'back') {
        card_text.innerHTML = front;
        card_text.className = 'front';
    }
}

function set_flashcard_content() {
    card_text.className = 'front';
    [front, back] = get_current_flashcard(current_flashcard_index);
    card_text.innerHTML = front;
}

function next_card() {
    if (current_flashcard_index < max_flashcard_index) {
        current_flashcard_index++;
        set_flashcard_content();
        update_flashcard_number();
    }
}

function previous_card() {
    if (current_flashcard_index > 0) {
        current_flashcard_index--;
        set_flashcard_content();
        update_flashcard_number();
    }
}

function is_focused(element) {
    return (element === document.activeElement);
}

function animation_restart() {
    card.classList.remove('card_animation');
    void card.offsetWidth;
    card.classList.add('card_animation');
}

function animation_stop() {
    card.classList.remove('card_animation');
}

card.addEventListener('click', () => {
    set_flashcard_side();
    animation_restart();
});
button_next.addEventListener('click', () => {
    next_card();
    animation_stop();
});
document.addEventListener('keydown', (event) => {
    if (event.keyCode === 39) {
        next_card();
        animation_stop();
    }
});
button_previous.addEventListener('click', () => {
    previous_card();
    animation_stop();
});
document.addEventListener('keydown', (event) => {
    if (event.keyCode === 37) {
        previous_card();
        animation_stop();
    }
});
document.addEventListener('keypress', (event) => {
    if (event.keyCode === 32 && !(is_focused(button_next) || is_focused(button_previous))) {
        set_flashcard_side();
        animation_restart();
    }
})

init_training();