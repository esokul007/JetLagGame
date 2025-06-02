from flask import Flask, render_template, request, redirect, url_for, session, flash
import random, sys, os, sqlite3
import cards, db

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods=['GET', 'POST'])
def home():
        if 'username' not in session:
                session['username'] = ""
                session['all_cards'] = ""
                session['drawn'] =""
        else:
                session['all_cards'] = db.getCards(session['username'])
        username = session['username']
        all_cards= session['all_cards']
        press = False
        card = session['drawn']
        if request.method == 'POST':
                press = request.form.get('random')
                if request.form.get('add'):
                        if isinstance(card, str):
                                db.addCard(username,card)
                        else:
                                db.addCard(username, card[0])
                if press:
                        card = cards.select()
                        session['drawn'] = card
                if request.form.get('user'):
                        username = request.form['username']
                        session['username'] = username
                        db.addUser(username)
                if request.form.get('rm'):
                        rm_card = request.form['remove']
                        db.remCard(username, rm_card)
                all_cards = db.getCards(username)
                session['all_cards'] = all_cards
        #print(username)
        return render_template("home.html", card = card, press = press, username = username, all_cards = all_cards)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
