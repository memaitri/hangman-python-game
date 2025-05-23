from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

from hangman_art import logo, stages
from hangman_words import word_list

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'word' not in session:
        session['word'] = random.choice(word_list)
        session['display'] = ['_'] * len(session['word'])
        session['lives'] = 6
        session['guessed'] = []

    message = ""
    if request.method == 'POST':
        guess = request.form['guess'].lower()
        if guess in session['guessed']:
            message = f"You already guessed '{guess}'!"
        else:
            session['guessed'].append(guess)
            if guess in session['word']:
                for i, letter in enumerate(session['word']):
                    if letter == guess:
                        session['display'][i] = guess
                if '_' not in session['display']:
                    message = "🎉 You Win!"
            else:
                session['lives'] -= 1
                message = f"'{guess}' is not in the word. You lost a life."
                if session['lives'] == 0:
                    message = f"💀 You lose. The word was '{session['word']}'."
    
    return render_template('index.html',
                           logo=logo,
                           display=' '.join(session['display']),
                           lives=session['lives'],
                           stage=stages[session['lives']],
                           guessed=session['guessed'],
                           message=message)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
