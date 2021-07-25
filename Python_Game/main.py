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

	def start_game(self):
		while (self.live_game):
			self.step_game()
	
	def	check_win_good_team(self):
		if (self.bad_team.get_full_damage_team <= self.good_team.get_xp_team or self.bad_team.cnt_in_live <=0):
			return True
		return False

	def	check_win_bad_team(self):
		if (self.good_team.get_full_damage_team <= self.bad_team.get_xp_team or self.good_team.cnt_in_live <=0):
			return True
		return False

	def step_game(self):
		if (self.live_game == False):
			return
		print(self.good_team)
		print(self.bad_team)
		self.good_team.attack(self.bad_team)
		if (self.check_win_good_team()):	
			self.live_game = False
			print(GREEN + self.good_team.name_team + " it's win!!! ")
			return
		self.bad_team.attack(self.good_team)
		if (self.check_win_bad_team()):
			self.live_game = False
			print(GREEN + self.bad_team.name_team + " it's win!!! ")
			return
		print(self.good_team)
		print(self.bad_team)



try:
	game = Random_Game("Fcb", "Terror")
	game.start_game()

except  BaseException as e:
	print("Error!")
	print(e)
