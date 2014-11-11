#calculate_best.py
#written to calculate the best player for all the games in the xml file.


import xml.etree.ElementTree as ET

#			determine_score - takes a player and returns a tuple of his
#							  number, score, and teamname in that order
def determine_score(p, teamname):
	trys = int(p.find('trys').text)
	pks = int(p.find('penaltykicks').text)
	cks = int(p.find('conversions').text)
	tackles = int(p.find('tackles').text)
	carries = int(p.find('carries').text)
	ypc = float(p.find('yardspercarry').text)
	yards = int(p.find('totalyards').text)
	knocks = int(p.find('knocks').text)
	penalties = int(p.find('penalties').text)	
	score = (trys*30) + (cks*3) + (pks*5) + (yards*.1) + (knocks*-10) + (penalties*-5) + (ypc*7) + (tackles*4) + (carries*1)
	return [p.find('number').text, score, teamname.text]


#open the tree
tree = ET.parse('gamedata.xml')
data = tree.getroot()
#iterate over each game
for game in data:
	#man is a structure who's values correspond to player number, score, and team name
	man = [0,-1,'']
	teams = []
	#iterate over each player on both teams, then determine the winner by the highest score.
	for team in game:
		teams.append([team.find('name').text, team.find('score').text])
		for player in team:
			if player.tag != 'player':
				continue
			guy = determine_score(player, team.find('name'))
			if guy[1] > man[1]:
				man = guy
	print(teams[0][0] + ': ' + teams[0][1] + '\n' + teams[1][0] + ': ' + teams[1][1] + '\n Man of the Match: \n' + man[2] + ' #' + str(man[0]) + '\n')