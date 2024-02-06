# Flashcards App
App to make and train on your own flashcards. Quizlet clone.

## Description
<br>This project is web app, where a user can make his own flashcards and then train on them. After signing or logging in, a user can go to a Train page of the app, where he can create new collections, edit or remove existing ones and learn from them 
with option of pseudo random collection shuffling. At this moment users don't have any access to other users collections, whether they want them to be public or private, but it will change soon.<br>
<br>The app is using simple authorization, where username has to be unique. User credentials and flashcard information are stored in SQLite database, created with SQLAchemy.
Users' passwords are stored encrypted. The app backend is made with python Flask microframework. Templates are made with HTML5 and Jinja2, and the rest of frontend is done with plain CSS and javascript.<br>

## Installation

Currently the app is not hosted, so if you want to try it, you have to install it on your own workstation.

### Cloning

Firstly, you have to clone repository into directory where you want it to be.
```bash
git clone https://github.com/iszablowski/flashcards_app.git
```

### Virtual environment

I recommend you setting up virtual environment before installing packages. You can choose any virtual environment you want, but if you have never worked with one, [here's the link](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) for the tutorial how to set it up. You should be setting it in the main directory.

### Modules

After setting up your virtual environment successfully, you need to install all additional python packages for the app to work. There is a `install_requirements.sh` script in the main directory. After running this script you will have all packages required for this project.

### Setting environment variables for app

I suggest making a `.env` file in your main directory, and putting your variables there, but you can also set it with Bash built-in export command.\
If you want to be able to start your app with `flask run` from the main directory, set your variable like this.
```bash
FLASK_APP=src/application
```
