from Color import Color
import time
import random

from abc	import ABCMeta, abstractmethod, abstractproperty
from typing import ClassVar, TypeVar

Weapon = TypeVar('Weapon')

class Weapon(metaclass = ABCMeta):
	
	def __init__(self) -> None:
		self.accuracy = 0
		self.damage = 0 
		self.time_recharge = 0
		self.ammunition = 0
		self.name = ''
	
	@abstractmethod
	def shoot(self, obj):
		pass
	
	
	def __str__(self) -> str:
		st = ''
		st += Color.GRAY
		st += "Name Weapon: " + self.name + '\n'
		st += "Accuracy: " + str(self.accuracy) + '\n'
		st += "Damage: " + str(self.damage) + '\n'
		st += "Time_recharge: " + str(self.time_recharge) + '\n'
		st += "Ammunition: " + str(self.ammunition) + '\n'
		st += Color.FONE
		return st

	@property
	def full_damage(self):
		return (self.damage * self.ammunition)

	def __eq__(self, other):
		return (self.name == other.name)

	# !=
	def __ne__(self, other):
		if (self == other):
			return False
		else:
			return True	
	# <=
	def __lt__(self, other):
		if (self.full_damage < other.full_damage):
			return (True)

	# >=
	def __gt__(self, other):
		if (self.full_damage < other.full_damage):
			return (False)
	
	
	def __cmp__(self, other:Weapon):
		if (self.name == other.name):
			return (0)
		if( self.damage * self.ammunition < other.damage * other.ammunition):
			return (-1)
		else:
			return (1)	



class 	Automat(Weapon):
	

	def __init__(self):
		self.name = 'Automat'
		self.accuracy = 0.4
		self.damage = 14
		self.time_recharge = 0.8
		self.ammunition = 14
	
	def shoot(self, obj):
		if (self.ammunition <= 0):
			print(Color.RED + "END Ammunition!(" + Color.FONE)
		else:
			if (random.random() < self.accuracy):
				obj.takeDamage(self)
			else:
				print(Color.RED + "I didn't get it" + Color.FONE)
			self.ammunition -= 1	
			self.__recharge()

	
	# Private Methods
	def __recharge(self):
		print(Color.PURPULE + "Recharge Automat")
		time.sleep(self.time_recharge)
		print("Recharge Automat END\n" + Color.FONE)

class 	Automat_Gun(Weapon):
	

	def __init__(self):
		self.name = 'Automat_Gun'
		self.accuracy = 0.5
		self.damage = 9
		self.time_recharge = 0.7
		self.ammunition = 12
	
	def shoot(self, obj):
		if (self.ammunition <= 0):
			print(Color.RED + "END Ammunition!(" + Color.FONE)
		else:
			if (random.random() < self.accuracy):
				obj.takeDamage(self)
			else:
				print(Color.RED + "I didn't get it" + Color.FONE)
			self.ammunition -= 1	
			self.__recharge()

	
	# Private Methods
	def __recharge(self):
		print(Color.PURPULE + "Recharge Automat")
		time.sleep(self.time_recharge)
		print("Recharge Automat END\n" + Color.FONE)


class 	Gun(Weapon):
	
	def __init__(self):
		self.name = 'Gun'
		self.accuracy = 0.5
		self.damage = 6
		self.time_recharge = 0.3
		self.ammunition = 8
	
	def shoot(self, obj):
		if (self.ammunition <= 0):
			print(Color.RED + "END Ammunition!(" + Color.FONE)
		else:
			if (random.random() < self.accuracy):
				obj.takeDamage(self)
			else:
				print(Color.RED + "I didn't get it" + Color.FONE)
			self.ammunition -= 1	
			self.__recharge()
	## TODO:Заменить метод Recharge на декоратор
	# Private Methods
	def __recharge(self):
		print(Color.PURPULE + "Recharge Gun")
		time.sleep(self.time_recharge)
		print("Recharge Automat END\n" + Color.FONE)


class Stick(Weapon):
	
	def __init__(self):
		self.name = 'Stick'
		self.accuracy = 1
		self.damage = 1
		self.time_recharge = 1
		self.ammunition = 10
	
	def shoot(self, obj):
		if (self.ammunition <= 0):
			print(Color.RED + "Stick is break!(" + Color.FONE)
		else:
			obj.takeDamage(self)			
			self.__recharge()

	# Private Methods
	def __recharge(self):
		print(Color.PURPULE + "Recharge Stick")
		time.sleep(self.time_recharge)
		print("Recharge Srick END\n" + Color.FONE)



