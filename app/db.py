import sqlite3
import csv
from datetime import datetime

DB_FILE = "players.db"
def setup():
	db = sqlite3.connect(DB_FILE, check_same_thread=False)
	c = db.cursor()
	c.execute("DROP TABLE users;")
	c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL UNIQUE, card1 TEXT, card2 TEXT,card3 TEXT,card4 TEXT,card5 TEXT, question TEXT, sentAt TEXT, draws INTEGER, picks INTEGER, cursed BOOLEAN);")
 # c.execute("CREATE TABLE IF NOT EXISTS gameChallenge (challenge_ID INTEGER PRIMARY KEY AUTOINCREMENT, chal>
 # c.execute("CREATE TABLE IF NOT EXISTS gameHistory (game_ID INTEGER PRIMARY KEY, winner TEXT, loser TEXT);>
 # c.execute("CREATE TABLE IF NOT EXISTS gameTracker (game_ID INTEGER, player1 TEXT, player2 TEXT, move1 TE

	db.commit()
	db.close()

# Reset DB
#setup()

def addUser(user):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("INSERT or IGNORE INTO users (username, draws, picks, question, sentAt) VALUES (?, ?, ?, ?, ?)",(user, 0, 0, "", ""))
    db.commit()
    db.close()

def addCard(user, card):
    index=4
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT card1, card2, card3, card4, card5 FROM users WHERE username = (?)", (user,))
    result=c.fetchone()
    for i in range(len(result)):
        if result[i] == None:
            index=i
            break
    c.execute(f"UPDATE users SET card{index + 1} = ? WHERE username = ?", (card, user))
    print(result)
    db.commit()
    db.close()

def getAllUsers():
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT username FROM users")
    result=c.fetchall()
    return (result)
    db.commit()
    db.close()

def remCard(user, card):
	index = None
	db = sqlite3.connect(DB_FILE, check_same_thread=False)
	c = db.cursor()
	c.execute("SELECT card1, card2, card3, card4, card5 FROM users WHERE username = (?)", (user,))
	result=c.fetchone()
	for i in range(len(result)):
		if isinstance(result[i], str):
			parts = result[i].split(" / ")
			if parts[0] ==card:
				index=i + 1
				break
	if index != None:
		c.execute(f"UPDATE users SET card{index} = ? WHERE username = ?", (None, user))
	db.commit()
	db.close()
def getCards(user):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT card1, card2, card3, card4, card5 FROM users WHERE username = (?)", (user,))
    result=c.fetchone()
    db.commit()
    db.close()
    return result

def getDraws(user):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT draws FROM users WHERE username = (?)", (user,))
    result=c.fetchone()
    db.commit()
    db.close()
    print(result)
    return result[0]

def getPicks(user):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT picks FROM users WHERE username = (?)", (user,))
    result=c.fetchone()
    db.commit()
    db.close()
    return result[0]

def getQuestion(user):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT question FROM users WHERE username = (?)", (user,))
    result=c.fetchone()
    db.commit()
    db.close()
    return result[0]


def getCursed(user):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT cursed FROM users WHERE username = (?)", (user,))
    result=c.fetchone()
    db.commit()
    db.close()
    return result[0]

def getSentAt(user):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT sentAt FROM users WHERE username = (?)", (user,))
    result=c.fetchone()
    db.commit()
    db.close()
    return result[0]

    result=c.fetchone()
    db.commit()
    db.close()
    return result[0]
	
def sendQuest(user, question, draws, picks):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("UPDATE users SET question = ?, sentAt = ?, draws = ?, picks = ? WHERE username = ?", (question, datetime.utcnow(), draws, picks, user))
    db.commit()
    db.close()


def setDraws(user, draws):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("UPDATE users SET draws = ? WHERE username = ?", (draws, user))
    db.commit()
    db.close()

def setPicks(user, picks):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("UPDATE users SET picks = ? WHERE username = ?", (picks, user))
    db.commit()
    db.close()

def setQuestion(user, question):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("UPDATE users SET question = ? WHERE username = ?", (question, user))
    db.commit()
    db.close()

def setCursed(user):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("UPDATE users SET cursed = ? WHERE username = ?", (True, user))
    db.commit()
    db.close()
