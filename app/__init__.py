from flask import Flask, render_template, request, redirect, url_for, session, flash
import random, sys, os, sqlite3
import cards

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods=['GET', 'POST'])
def home():
	press = False
	card = ""
	if request.method == 'POST':
                press = request.form.get('random')
                card = cards.select()
	return render_template("home.html", card = card, press = press)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
