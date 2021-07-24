from random import randint
from typing import ClassVar
from Weapon import *
from Person import *
from Teams  import *

class Random_Game:

	def __init__(self, team1, team2):
		self.good_team = FCB(team1, random.randint(1, 3))
		self.bad_team = Terrorist(team2, random.randint(1, 3))
		self.live_game = True

	def step_game(self):
		print(self.good_team)
		print(self.bad_team)
		self.good_team.attack(self.bad_team)
		if (self.bad_team.get_full_damage_team <= self.good_team.get_xp_team or self.bad_team.cnt_in_live <=0):
			self.live_game = False
			print(GREEN + self.good_team.name_team + " it's win!!! ")
			return
		self.bad_team.attack(self.good_team)
		if (self.good_team.get_full_damage_team <= self.bad_team.get_xp_team or self.good_team.cnt_in_live <=0):
			self.live_game = False
			print(GREEN + self.bad_team.name_team + " it's win!!! ")
			return
		print(self.good_team)
		print(self.bad_team)

game = Random_Game("Fcb", "Terror")
while (game.live_game):
	game.step_game()		

# try:
# 	game = Random_Game("Fcb", "Terror")
	
# 	while (game.live_game):
# 		game.step_game()

# except  BaseException as e:
# 	print("Error!")
# 	print(e)
