const set_username_btn = document.querySelector('#set-username-btn');
const user_information = document.querySelector('#new-usrnm');
const submit_button = document.querySelector('.submit');

function show_set_username_forms() {
    user_information.setAttribute("type", "text");
    submit_button.removeAttribute("hidden");
}

set_username_btn.addEventListener('click', show_set_username_forms);