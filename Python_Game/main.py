#! /usr/local/bin/python3 

from random import randint
from typing import ClassVar
from Weapon import *
from Person import *
from Teams  import *

import sys, os


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
			print(Color.GREEN + self.good_team.name_team + " it's win!!! " + Color.FONE)
			return
		self.bad_team.attack(self.good_team)
		if (self.check_win_bad_team()):
			self.live_game = False
			print(Color.GREEN + self.bad_team.name_team + " it's win!!! " + Color.FONE)
			return
		print(self.good_team)
		print(self.bad_team)


def main():
	
	if (len(sys.argv) >= 2):
		game = Random_Game("Fcb", "Terror")
		game.start_game()
	sys.exit(42)
	
	#print(dir(Weapon()))
	#pers  = Hero('dsf', Gun(), xp = -2)
	#print(help(print_err))

	while(1):
		pass
	#print(1/0)

	#gun = Gun()
	#gun._recharge()	
	# Как сделать чтобы выше не запускалось
try:
	if __name__ == "__main__":
		main()

except  BaseException as e:
	print_err(e)
	if (type(e) == SystemExit):
		sys.exit(e)
	