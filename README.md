# Flashcards App
App to make and train on your own flashcards. Quizlet clone.

## Description
<br>This project is web app, where user can make his own flashcards and then train on them. After signing or logging in, user can go to Train page of the app, where he can create new collections, edit or remove existing ones, and learn from them 
with option of pseudo random collection shuffling. At this time users don't have access to other users collections, whether if they want them to be public or private, but it will change in near time.<br>
<br>App is using simple authorization, where username have to be unique. User credentials and flashcards information are stored in SQLite database, created with SQLAchemy.
Users passwords are stored encrypted. App backend is made with python Flask microframework. Templates are made with HTML5 and Jinja2, and the rest of frontend is done with plain CSS and javascript.<br>

## Installation

Currently app is not hosted, so if you want to try it, you have to install it on your workstation.

### Cloning

Firstly, you have to clone repository into directory you want it to be.
```bash
git clone https://github.com/iszablowski/flashcards_app.git
```


### Virtual environment

I recommend you setting up virtual environment before installing packages. You can choose any virtual environmentm you want, but if you have never worked with one, [here's the link](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) for tutorial how to set it up.

### Modules
