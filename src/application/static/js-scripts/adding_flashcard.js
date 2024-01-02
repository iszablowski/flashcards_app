const add_row_btn = document.querySelector('#add-row-btn');
const flashcard_row = document.querySelector('.flashcard-row');
const all_flashcards = document.querySelector('.all-flashcards');

function clear_inputs(inputs) {
    inputs.forEach((input) => {
        input.value = '';
    });
}

function add_row() {
    let new_row = flashcard_row.cloneNode(true);
    clear_inputs(new_row.querySelectorAll('input[type=text]'));
    all_flashcards.appendChild(new_row);
}

add_row_btn.addEventListener('click', add_row);