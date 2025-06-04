import random
curse={
    "Curse of The Zoologist": ['photo of an animal', "Take a photo of a wild fish, bird, mammal, reptile, amphibian or bug. The seeker(s) must take a picture of a wild animal in the same category before  asking another question."],
    "Curse Of The Unguided Tourist" : ['Seeker(s) must be outside', "Send the seeker(s) an unzoomed google Street View image from a street within 500ft (152m) of where they are now. The shot has to be parallel to the horizon and include at least one human-built structure other than a road. Without using the internet for research, they must find what you sent them in real life before they can use transportation or ask another question. They must send a picture the hiders for verification."],
    "Curse of The Endless Tumble" : ["Send the seeker(s) an unzoomed google Street View image from a street within 500ft (152m) of where they are now. The shot has to be parallel to the horizon and include at least one human-built structure other than a road. Without using the internet for research, they must find what you sent them in real life before they can use transportation or ask another question. They must send a picture the hiders for verification.", "Seekers Must roll a die at least 100ft (30m) and have it land on a 5 or a 6 before they can ask another question. The die must roll the full distance, unaided, using only the momentum from the initial throw and gravity to travel the 100ft (30m). If the seekers accidentally hit someone with a die you are awarded a [S10, M20, L30] minute bonus"],
    "Curse of the Hidden Hangman" : ["Discard 2 cards", "Before asking another question or boarding another form of transportation, seeker(s) must be the hider(s) in game of hangman."],
    "Curse of the Overflowing Chalice" : ["Discard a card", "For the next three questions, you may draw (not keep) an additional card when drawing from the hider deck"],
    "Curse of the Mediocre Travel Agent" : ["None", "Choose any publicly-accessible place within [S0.25, M0.25, L0.50]mi [S0.40, M0.40, 0.50]km of the seeker(s) current location. They cannot currently be on transit. They must go there, and spend at least [S5, M5, L10] minutes there, before asking another question. They must send you at least three photos of them enjoying their vacation, and procure an object to bring you as souvenir. If this souvenir is lost before they can get to you, you are awarded and extra [S30, M45, L60] minutes."],
    "Curse of The Luxury Car" : ["A photo of a car", "Take a photo of a car. The seekers must take a photo of a more expensive car before asking another question."],
    "Curse of The U-Turn" : ["Seekers must be heading the wrong way. (Their next station is further from you then they are.)", "Seeker(s) must disembark their current mode of transportation at the next station (as long as that station is served by another form of transit in the next [S0.5, M0.5, L1] hours"],
    "Curse of the Bridge Troll" : ["Seekers Must be at least [S1, M5, L30]mi [S0.3, M1.5, L9.1]km from you", "The seekers must ask their next question from under a bridge"],
    "Curse of Water Weight" : ["Seekers must be within 1,000ft (300 meters) of a body of water", "Seeker(s) must acquire and carry at least 2 liters of liquid per seeker for the rest of your run. They cannot ask another question until they have acquired the liquid. The water may be distributed between seeker as they see fit. If the liquid is lost or abandoned at any point the hider is awarded a [S30, M30, L60] minute bonus"],
    "Curse of The Jammed Door" : ["Discard 2 cards" , "For the next [S0.5, M1, L3] hours, whenever the seeker(s) want to pass through a doorway into a building, business, train, or other vehicle they must first roll 2 dice. If they do not roll a 7 or higher they cannot enter that space (including through other doorways) any given doorway can be reattempted after [S5, M10, L15] minutes."],
    "Curse of The Cairn" : ["Build A rock tower", "You have one attempt to stack as many rocks on top of each other as you can in a freestanding tower. Each rock may only touch one other rock. Once you have added a rock to the tower it may not be removed. Before adding another rock, the tower must stand for at least 5 seconds. If at any point any rock other then the base rock touches the ground, your tower has fallen. Once your tower falls tell the seekers how many rocks high your tower was when it last stood for five seconds. The seekers must then construct a rock tower of the same number of rucks, under the same parameters before asking another question. If their tower falls they must restart. The rocks must be found in nature and both teams must  disperse the rocks after building."],
    "Curse of The Urban Explorer" : ["Discard 2 Cards", "For the rest of the run seekers cannot ask question when they are on transit or in a train station"],
    "Curse of The Impressionable Consumer" : ["The seekers next question is free", "Seekers must enter and gain admission (if applicable) to a location or buy a product that they saw an advertisement for before asking another question. This advertisement musts be found out in the world and must be at least 100ft (30m) from the product or location itself."],
    "Curse of The Egg Partner" : ["Discard Two Cards", "Seeker(s) must acquire an egg before asking another question. This egg is now treated as an official team member of the seekers. If any team members are abandoned or killed (defined as crack in the eggs case) before the end of your run you are awarded an extra [S30 M45 L60] minutes. This course cannot be played during the endgame."],
    "Curse of The Distant Cuisine" : ["You must be at the restaurant", "Find a restaurant within your zone that explicitly serves food from a specific foreign country. The seekers must visit a restaurant serving food from a country that is equal or great distance away before asking another question"],
    "Curse of the Right Turn" : ["Discard a Card", "For the next [S20, M40, L60] minutes the seekers can only turn right at any street intersection. If at any point they find themselves in dead end where they cannot continue forward or turn right for another 1,000ft (304m) they must do a full 180. A right turn is defined as a road at any angle that veers to the right of the seekers"],
    "Curse of The Labyrinth" : ["Draw a maze", "Spend up to [S10, M20, L30] minutes drawing a solvable maze and send a photo of it to the seekers. You cannot use the internet to research maze designs. The seekers musts solve the maze before asking another question."],
    "Curse of The Bird Guide" : ["Find A Bird", "You have one chance to film a bird for as long as possible. Up to [S5 M10 L15] minutes straight, if at any point the bird leaves the frame your timer is stopped. The seekers must then film a bird for the same amount of time or longer"],
    "Curse of Spotty Memory" : ["Discard a time bonus card", "For the rest of the run, one random category of questions will be disabled at all times. After this curse is played seeker(s) must roll a die to determine the category of questions to be disabled. The catergy remain disabled until the next question is asked at which point a die is rolled again to choose an e category. The same category can be disabled multiple times in a row"],
    "Curse of The Lemon Phylactery" : ["Discard a powerup card", "Before asking another question the seeker(s) must each find a lemon and affix it to their outermost layer of their clothes or skin. If at any point one of these lemons is no longer touching a seeker you are awarded  [S30, M45, L60] minutes. This curse cannot be played during the endgame."],
    "Curse of The Drained Brain" : ["Discard your hand", "Choose three questions in different categories. The seekers cannot ask those questions for the rest of the run."],
    "Curse of the Ransom Note" : ["Spell out 'Ransom Note' as a ransom note", "The next question that the seekers ask must be composed of words and letters cut out of any printed material. The question must be coherent and include at least 5 words."],
    "Curse of The Gambler's Feet" : ["Roll a die if it's even, this curse has no effect", "For the next [S20, M40, L60] minutes seekers must roll a die before they take any steps in any direction, they may take that many steps before rolling again"]
}
questions={
	"Matching":{
		"template": "Is your nearest _____ the same as my nearest _____?",
		"filters": ["Airport", "Train Station", "Station name length", "town", "borough", "landmass", "park", "zoo", "aquarium", "museum", "movie theatre", "hospital", "library"],
		"draw": 3,
		"pick":1
		},
	"Measuring":{
		"template":"Compared to me, are you closer to or further from _____?",
                "filters": ["Airport", "Train Station", "Station name length", "town", "borough", "landmass", "park", "zoo", "aquarium", "museum", "movie theatre", "hospital", "library"],
                "draw": 3,
                "pick":1
                },
        "Thermometer":{
                "template":"I just traveled (at least) _____. Am I hotter or colder?",
                "filters": ["0.5 mi", "3 mi", "10 mi"],
                "draw": 2,
                "pick":1
                },
        "Radar":{
                "template":"Are you within _____ of me?",
                "filters": ["0.25 mi", "0.5 mi", "1 mi", "3 mi", "5 mi", "10 mi", "25 mi", "50 mi", "100 mi"],
                "draw": 2,
                "pick":1
                },
        "Tentacles":{
                "template":"Of all the _____s within 1 mile of me, which are you closest to?",
                "filters": ["Airport", "Train Station", "town", "borough", "landmass", "park", "zoo", "aquarium", "museum", "movie theatre", "hospital", "library"],
                "draw": 4,
                "pick":2
                },
        "Photos":{
                "template":"Send a Photo of _____",
                "filters": ["a tree", "the sky", "the widest street", "the tallest structure in your sightline", "any building visible from station", "the tallest building visible from your station", "trace of nearest street/path", "two buildings", "restaurant interior", "a train platform", "a park", "a grocery store aisle", "a place of worship"],
                "draw": 1,
                "pick":1
                },
	}
cards={"3 min": 25,
       "6 min": 15,
       "9 min": 10,
       "12 min": 3,
       "18 min": 2,
       "Randomize": 4,
       "Veto": 4,
       "Duplicate": 2,
       "Move": 1,
       "Discard 1 Draw 2": 4,
       "Discard 2 Draw 3": 2,
       "Draw 1 Expand 1": 2,
       "curse":24}
def select():
	card = list(cards.keys())
	chance = list(cards.values())

	selection = random.choices(card, weights=chance, k=1)[0]
	if selection == "curse":
    		random_key = random.choice(list(curse.keys()))
    		random_pair=(random_key, curse[random_key])
    		selection = random_pair
	return selection
