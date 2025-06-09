from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import random, sys, os, sqlite3
import cards, db

app = Flask(__name__)
app.secret_key = os.urandom(32)
questions = cards.questions

@app.route('/', methods=['GET', 'POST'])
def home():
        if 'username' not in session:
                session['username'] = ""
                session['all_cards'] = ""
                session['drawn'] =[]
                session['show'] = False
                session['question'] = ""
                session['sentAt'] = ""
                session['draws'] = 0
                session['picks'] = 0
                session['cursed'] = False
                session['curseCard']=""
        elif session['username'] != '':
                session['all_cards'] = db.getCards(session['username'])
                session['draws'] = db.getDraws(session['username'])
                session['picks'] = db.getPicks(session['username'])
                session['question'] = db.getQuestion(session['username'])
                session['sentAt'] = db.getSentAt(session['username'])
                session['cursed'] = db.getCursed(session['username'])
                session['curseCard'] = db.getCurseCard(session['username'])
        all_users = db.getAllUsers()
        username = session['username']
        all_cards= session['all_cards']
        show=session['show']
        card = session['drawn']
        question = session['question']
        sentAt = session['sentAt']
        cursed = session['cursed']
        curseCard = session['curseCard']
        draws = session['draws']
        picks = session['picks']
        if request.method == 'POST':
                rm = request.form.get('rm')
                signIn = request.form.get('user')
                press = request.form.get('random')
                added = request.form.get('add')
                if request.is_json:
                        data=request.get_json()
                        if data.get('action') == "swipe":
                                card=data.get('card')
                                recipient=data.get("user")
                                parts=card.split(' / ') # Just take curse name
                                print(recipient)
                                db.remCard(username, parts[0])
                                if recipient:
                                        db.setCursed(recipient, True, card)
                                        # db.addCard(recipient, card)
                                return jsonify(success=True)
                for key in questions:
                        if request.form.get("submit") and request.form.get(key) != None:
                                send = questions[key]['template']
                                draws = questions[key]['draw']
                                picks = questions[key]['pick']
                                send = send.replace("_____", request.form.get(key))
                                send_to_user = request.form['send']
                                print(send_to_user)
                                if send_to_user != username:
                                        db.sendQuest(send_to_user, send, draws, picks)
                                # print(send, request.form["send"])

                if added:
                        if added[0] != '(': # eliminates the curses
                                db.addCard(username,added)
                        else:
                                parsed = eval(added)
                                db.addCard(username, parsed[0] + " / " + parsed[1][1])
                        session['drawn'] = []
                if press and draws > 0:
                        for i in range(draws):
                                card.append(cards.select())
                        session['drawn'] = card
                        session['show'] = True
                        session['draws'] = 0
                        db.setDraws(session['username'], session['draws'])
                if signIn:
                        username = request.form['username']
                        session['username'] = username
                        db.addUser(username)
                        print(1)
                if rm:
                        parts=rm.split(' / ') # Just take curse name
                        db.remCard(username, parts[0])
                all_cards = db.getCards(username)
                session['all_cards'] = all_cards

                return redirect(url_for('home'))
        #print(username)
        db.setCursed(username, False)
        session['show'] = False
        print(cursed)
        return render_template("home.html", card = card, show = show, username = username, all_cards = all_cards, questions = questions, draws= draws, question = question, picks = picks, allUsers= all_users, sentAt = sentAt, allowed_time = 300, cursed = cursed, curseCard = curseCard)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
