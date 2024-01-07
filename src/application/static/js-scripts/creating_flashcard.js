const add_row_btn = document.querySelector('#add-row-btn');
const flashcard_row = document.querySelector('.flashcard-row');
const all_flashcards = document.querySelector('.all-flashcards');
const remove_row_btn = document.querySelector('#remove-row-btn');

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

function remove_row() {
    let rows = document.querySelectorAll('.flashcard-row');
    if (rows.length > 1) {
        rows[rows.length-1].remove();
    }
}

function scroll_smooth_to_bottom() {
    window.scrollTo({left: 0, top: document.body.scrollHeight, behavior: 'smooth'});
}

add_row_btn.addEventListener('click', add_row);
add_row_btn.addEventListener('click', scroll_smooth_to_bottom);
remove_row_btn.addEventListener('click', remove_row);