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
                session['show'] = False
        else:
                session['all_cards'] = db.getCards(session['username'])
        username = session['username']
        all_cards= session['all_cards']
        show=session['show']
        card = session['drawn']
        if request.method == 'POST':
                rm = request.form.get('rm')
                signIn = request.form.get('user')
                press = request.form.get('random')
                added = request.form.get('add')
                if added:
                        if isinstance(card, str):
                                db.addCard(username,card)
                        else:
                                print(card[0] + " / " + card[1][0])
                                db.addCard(username, card[0] + " / " + card[1][1])
                if press:
                        card = cards.select()
                        session['drawn'] = card
                        session['show'] = True
                if signIn:
                        username = request.form['username']
                        session['username'] = username
                        db.addUser(username)
                if rm:
                        rm_card = request.form['remove']
                        db.remCard(username, rm_card)
                all_cards = db.getCards(username)
                session['all_cards'] = all_cards

                return redirect(url_for('home'))
        #print(username)
        session['show'] = False
        return render_template("home.html", card = card, show = show, username = username, all_cards = all_cards)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
