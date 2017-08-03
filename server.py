from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsMySecret'

@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = random.randrange(0,101)
    return render_template('index.html')

@app.route('/randomGuess', methods=['POST'])
def play():
    userGuess = request.form['guess']
    print session['random'], userGuess
    if int(userGuess) == session['random']:
        return render_template('success.html', result = 'Perfect!', userGuess=userGuess)
    elif int(userGuess) > session['random']:
         return render_template('index.html', result = 'Too High!, try again', userGuess=userGuess)
    elif int(userGuess) < session['random']:
         return render_template('index.html', result = 'Too Low! try again', userGuess=userGuess)

@app.route('/correctGuess')
def reset():
    session.pop('random') #this removes the raondom key stored in session to create a new one
    return redirect('/')




app.run(debug=True)
