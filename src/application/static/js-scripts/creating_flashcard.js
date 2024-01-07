const add_row_btn = document.querySelector('#add-row-btn');
const flashcard_row = document.querySelector('.flashcard-row');
const all_flashcards = document.querySelector('.all-flashcards');
const remove_row_btn = document.querySelector('#remove-row-btn');
const remove_btn = document.querySelector('#remove-btn');

let new_row_index = 1;

function clear_inputs(inputs) {
    inputs.forEach((input) => {
        input.value = '';
    });
}

function add_row() {
    let new_row = flashcard_row.cloneNode(true);
    clear_inputs(new_row.querySelectorAll('input[type=text]'));
    new_row.setAttribute('value', new_row_index);
    let new_button = new_row.querySelector('#remove-btn');
    new_button.value = new_row_index;
    new_button.addEventListener('click', remove_row);
    all_flashcards.appendChild(new_row);
    new_row_index++;
}

function scroll_smooth_to_bottom() {
    window.scrollTo({left: 0, top: document.body.scrollHeight, behavior: 'smooth'});
}

function remove_row(e) {
    let rows = document.querySelectorAll('.flashcard-row');
    if (rows.length > 1) {
        let row = document.querySelector(`.flashcard-row[value='${e.currentTarget.value}']`);
        row.remove();
    }
}

add_row_btn.addEventListener('click', add_row);
add_row_btn.addEventListener('click', scroll_smooth_to_bottom);
remove_btn.addEventListener('click', remove_row);