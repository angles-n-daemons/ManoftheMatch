#generategames.py
from __future__ import division
import random
import xml.etree.cElementTree as ET

#The following functions take a random number and generate an instance 
#of the game for aspects that likely not equally distributed

def convert_to_trys(randnum):
	if randnum < 75:
		return 0
	if randnum < 93:
		return 1
	if randnum < 97:
		return 2
	if randnum < 99:
		return 3
	if randnum < 100:
		return 4
	return 5

def convert_to_kicks(randnum):
	if randnum < 90:
		return 0
	if randnum < 92:
		return 1
	if randnum < 98:
		return 2
	if randnum < 100:
		return 3
	return 4

def convert_to_distance(randnum):
	if randnum < 700:
		return random.randint(-5,5)
	if randnum < 850:
		return random.randint(6,15)
	if randnum < 950:
		return random.randint(16,25)
	if randnum < 980:
		return random.randint(26,45)
	if randnum < 990:
		return random.randint(46,70)
	if randnum < 996:
		return random.randint(71,90)
	return random.randint(91,109)


#Initializing the xml tree and teams.
data = ET.Element("data")
teams = ['American International College', 'Boston College', 'University of Connecticut', 'Northeastern', 'Middlebury College']

#Iterate over each team to produce games against UMass
for i in range(len(teams)):
	game = ET.SubElement(data, "game")
	#Create the two teams in the element tree
	for k in range(2):
		team = ET.SubElement(game, "team")
		name = ET.SubElement(team, "name")
		if k is 0:
			name.text = 'University of Massachusetts'
		if k is 1:
			name.text = teams[i]

		mom = ET.SubElement(team, "manofmatch")

		score = 0;
		#Create 22 players for each team
		for j in range(22):
			#this block randomly generates values for a players involvement in a game.
			#some functions are used to give more realistic probabilities for certain instances (eg 4 tries)
			tries = convert_to_trys(random.randint(1,100))
			pkicks = convert_to_kicks(random.randint(1,95))
			cvtk = random.randint(0,2)
			tackles = random.randint(2,40)
			carries = random.randint(3,35)
			knocks = random.randint(0,7)
			penalties = random.randint(0,4)


			total = 0;
			for l in range(carries):
				total = total + convert_to_distance(random.randint(1,1000))
			ypc = total/carries
			if cvtk > tries:
				cvtk = tries


			player = ET.SubElement(team,"player")
			number = ET.SubElement(player, "number")
			number.text = str(j+1)
			trys = ET.SubElement(player, "trys")
			trys.text = str(tries)
			pks = ET.SubElement(player, "penaltykicks")
			pks.text = str(pkicks)
			conversions = ET.SubElement(player,"conversions")
			conversions.text = str(cvtk)
			tack = ET.SubElement(player, "tackles")
			tack.text = str(tackles)
			carr = ET.SubElement(player,"carries")
			carr.text = str(carries)
			avg = ET.SubElement(player, "yardspercarry")
			avg.text = str(ypc)
			yards = ET.SubElement(player, "totalyards")
			yards.text = str(total)
			knock = ET.SubElement(player, "knocks")
			knock.text = str(knocks)
			pen = ET.SubElement(player, "penalties")
			pen.text = str(penalties)
			score = score + (tries*5) + (cvtk*2) + (pkicks*3)
		
		scr = ET.SubElement(team, "score")
		scr.text = str(score)
			
#writing the tree out
tree = ET.ElementTree(data)
tree.write("gamedata.xml")