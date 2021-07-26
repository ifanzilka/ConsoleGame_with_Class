from typing import ClassVar
from Weapon import *
from Person import *
from Color  import *
from typing import List

class Team(metaclass = ABCMeta):

	@abstractmethod
	def attack(self, obj):
		pass

	@abstractmethod	
	def takedamage(self, obj):
		pass
	
	@property
	def get_full_damage_team(self):
		damage = 0
		for i in self.arr_pers:
			damage += i.weapon.full_damage
		return (damage)	

	@property
	def cnt_in_live(self)-> int:
		cnt = 0
		for i in self.arr_pers:
			if i.live:
				cnt += 1
		return (cnt)

	@property
	def get_xp_team(self):
		xp = 0
		for i in self.arr_pers:
			xp += i.xp
		return (xp)

	def get_army_xp(self):
		ls = self.arr_pers
		ls.sort(key = lambda x: x.xp ,reverse= True)
		return (ls)

	def get_army_weapon(self):
		ls = self.arr_pers
		ls.sort(key= lambda x: x.weapon.full_damage ,reverse= True)
		return (ls)

	def __str__(self):
		st = ''
		st += Color.GRAY
		st += "Name Team: " + self.name_team + '\n'
		st += "Count person: " + str(self.cnt_team) + '\n'
		st += "Full famage team: " + str(self.get_full_damage_team) + '\n'
		st += "Live person: " + str(self.cnt_in_live) + '\n'
		st += "Xp in team: " + str(self.get_xp_team) + '\n'
		st += Color.FONE
		return (st)



class FCB(Team):

	def __init__(self, name, cnt_team = 40):
		self.name_team = name
		self.cnt_team = cnt_team
		self.arr_pers = self.__init_arr_pers()

	def __init_arr_pers(self):
		
		lst_pers = [ 0 for i in range(self.cnt_team)]
		for i in range(self.cnt_team):
			ran = random.random()
			if ran < 0.5:
				lst_pers[i] = Hero.standat_pers()
			elif ran < 0.8:
				lst_pers[i] = Hero("FCB " + str(i), Gun() if random.random() < 0.5 else Automat_Gun(), armor=random.randint(1, 9))
			else:
				lst_pers[i] = Hero("FCB " + str(i), Automat())
		return (lst_pers)	

	def __getmax_ammo_pers(self)-> Person:
		ls = self.get_army_weapon()
		return (ls[0])

	@property
	def __get_cnt_no_empty_pers(self):
		cnt = 0
		ls =  self.get_army_weapon()
		for i in ls:
			if (i.weapon.full_damage > 0):
				cnt += 1
		return (cnt)

	@property
	def __get_max_xp_pers(self)-> Person:
		ls = self.get_army_xp()
		return (ls[0])

	def takedamage(self, team:List[Person]):
		print(Color.RED + self.name_team + ": AAA attack for me!!!!" + Color.FONE)
		for i in team:
			pers = self.__get_max_xp_pers
			i.attack(pers)	

	def attack(self, obj:Team):
		pers = self.__getmax_ammo_pers()
		if (pers.weapon.full_damage <= 0):
			print(Color.RED + "Ammunition end(" + Color.FONE)
		else:
			ls = self.get_army_weapon()
			cnt_pers = random.randint(1, self.__get_cnt_no_empty_pers)
			mini_team = ls[:cnt_pers]
			print(Color.GREEN + self.name_team + ": Go to attack in " + str(cnt_pers) + " pers" + Color.FONE)
			obj.takedamage(mini_team)

class Terrorist(Team):

	def __init__(self, name, cnt_team = 40):
		self.name_team = name
		self.cnt_team = cnt_team
		self.arr_pers = self.__init_arr_pers()

	def __init_arr_pers(self):
		lst_pers = [ 0 for i in range(self.cnt_team)]
		for i in range(self.cnt_team):
			ran = random.random()
			if ran < 0.4:
				lst_pers[i] = Enemy.standat_pers()
			elif ran < 0.85:
				lst_pers[i] = Enemy("Bad boy " + str(i), Gun() if random.random() < 0.5 else Automat_Gun(), armor= random.randint(1, 10))
			else:
				lst_pers[i] = Enemy("Very bad boy " + str(i), Automat())
		return (lst_pers)	

	def __getmax_ammo_pers(self)-> Person:
		ls = self.get_army_weapon()
		return (ls[0])

	def __get_cnt_no_empty_pers(self):
		cnt = 0
		ls =  self.get_army_weapon()
		for i in ls:
			if (i.weapon.full_damage > 0):
				cnt += 1
		return (cnt)

	@property
	def __get_max_xp_pers(self)-> Person:
		ls = self.get_army_xp()
		return (ls[0])

	def takedamage(self, team:List[Person]):
		print(Color.RED + self.name_team + ": AAA attack for me!!!!" + Color.FONE)
		for i in team:
			pers = []
			if self.cnt_team > 1:
				pers = self.arr_pers[random.randint(1, self.cnt_team - 1 )]
			else:
				pers = self.arr_pers[0]
			i.attack(pers)	

	def attack(self, obj:Team):
		pers = self.__getmax_ammo_pers()
		if (pers.weapon.full_damage <= 0):
			print(Color.RED + "Ammunition end(")
		else:
			ls = self.arr_pers
			cnt_pers = random.randint(1, self.cnt_team)
			mini_team = ls[:cnt_pers]
			print(Color.GREEN + self.name_team + ": Go to attack in " + str(cnt_pers) + " pers")
			obj.takedamage(mini_team)