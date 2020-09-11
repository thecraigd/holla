from flask import Flask, render_template, url_for, request, redirect
import random

app = Flask(__name__)

traditionally_cool = ["The Eagles", "Cheap Trick", "Lynyrd Skynyrd", "Aerosmith", "Talking Heads", "AC/DC", "Metallica", "The Shirelles", "Guns n’ Roses", "Sly and the Family Stone", "Nirvana", "Queen", "The Beatles", "The Rolling Stones", "Pink Floyd", "The Supremes", "Public Enemy", "The Bangles", "The Who", "The Runaways", "Isley Brothers", "Trans Siberian Orchestra", "Duran Duran", "The Ting Tings", "Garbage", "Led Zeppelin", "Foghat", "Steve Miller Band", "The Animals", "George Thorogood and The Destroyers", "Cream", "ZZ Top", "The White Stripes", "Fleetwood Mac", "Steely Dan", "Whitney Houston", "Wu-Tang Clan", "T. Rex", "Natalie Imbruglia", "Disturbed", "Rage Against the Machine", "Billy Joel", "Stevie Nicks", "Kiss", "Rob Zombie", "Lit", "Matchbox 20", "3 Doors Down", "Nine Inch Nails", "Linkin Park", "The Strokes", "Father John Misty", "Fatboy Slim", "KoRn"]
less_cool = ["The Hives", "Coal Chamber", "Papa Roach", "The Prodigy", "Limp Bizkit", "Warren Zevon", "3OH!3", "Rammstein", "Len", "Hootie & the Blowfish", "Insane Clown Posse", "Powerman 5000", "Steve Winwood", "Crazy Town", "System of a Down", "Electric Light Orchestra", "Bone Thugs ‘n’ Harmony", "Natalie Merchant", "Dinosaur Jr.", "Celine Dion", "REO Speedwagon", "The Doobie Brothers", "Hall & Oates", "Abba", "Boston", "Bee Gees", "Bon Jovi", "Metallica", "Iron Maiden", "The Scorpions", "Rush", "Simply Red", "Jimmy Buffett", "Dido", "Dire Straits", "U2", "Coldplay", "The Proclaimers"]

@app.route('/')
def index():
	item1 = random.choice(less_cool)
	item2 = random.choice(traditionally_cool)

	return render_template('index.html', item1=item1, item2=item2)



if __name__ == "__main__":
	app.run(debug=True)