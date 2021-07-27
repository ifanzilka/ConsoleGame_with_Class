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
	
	def recharge_print(name):
		def outer(func):
			# инициализируем новую функцию
			def inner(self):
				print(Color.PURPULE + "Recharge " + self.name+ Color.FONE)
				func(self)
				print(Color.PURPULE + "Recharge " + self.name + " END\n" +  Color.FONE)
			return inner
		return outer

	# Тоже самое что и _recharg = recharge_print(_recharge)('')
	@recharge_print('')
	def _recharge(self):
		"""Call fun after shoot"""
		time.sleep(self.time_recharge)

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

	#класс задающий сеттеры и геттеры
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
			self._recharge()


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
			self._recharge()


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
			self._recharge()


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
			self.ammunition -= 1		
			self._recharge()
