import sqlite3
import csv
from datetime import datetime

DB_FILE = "players.db"
        
def setup():            
	db = sqlite3.connect(DB_FILE, check_same_thread=False)
	c = db.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL UNIQUE, card1 TEXT, card2 TEXT,card3 TEXT,card4 TEXT,card5 TEXT);")   
 # c.execute("CREATE TABLE IF NOT EXISTS gameChallenge (challenge_ID INTEGER PRIMARY KEY AUTOINCREMENT, chal>
 # c.execute("CREATE TABLE IF NOT EXISTS gameHistory (game_ID INTEGER PRIMARY KEY, winner TEXT, loser TEXT);>
 # c.execute("CREATE TABLE IF NOT EXISTS gameTracker (game_ID INTEGER, player1 TEXT, player2 TEXT, move1 TE

	db.commit()
	db.close()

def addUser(user): 
    db = sqlite3.connect(DB_FILE, check_same_thread=False)         
    c = db.cursor()
    c.execute("INSERT or IGNORE INTO users (username) VALUES (?)",(user,))
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
		print(result)
	db.commit()
	db.close()
def getCards(user):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT card1, card2, card3, card4, card5 FROM users WHERE username = (?)", (user,))
    result=c.fetchone()
    return result

remCard("Eastwood", "25")
