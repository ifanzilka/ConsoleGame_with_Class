from abc 		import ABCMeta, abstractmethod, abstractproperty
from typing 	import TypeVar
from Game_error import *
from Weapon 	import *

Person = TypeVar('Person')

class Person(metaclass = ABCMeta):
	
	#Эти Методы обязательно реализуем если нет, то "TypeError: Can't instantiate abstract class Hero with abstract methods foo"
	
	__slots__ = ['name', 'xp', 'weapon', 'live']

	# def __init__(self):
	# 	self.name = ''
	# 	self.xp = 0
	# 	self.weapon = 0
	# 	self.live = True

	@abstractmethod
	def attack(self):
		pass
	
	@abstractmethod
	def takeDamage(self, amount):
		pass

	def __str__(self)->str:
		st = ''
		st += Color.WHITE
		st += 'Person: ' + self._names + '\n'
		st += "Xp: " + str(self.xp) + '\n'
		st += "Weapon: " + self.weapon.name + '\n'
		st += "Live: " + str(self.live) + '\n'
		st += Color.FONE
		return (st)
	
	def __repr__(self) -> str:
		return ("<name: " + self._names + " Xp: " + str(self.xp) + " Weapon: " + repr(Weapon) + ">")
	
	def __format__(self, format_spec: str) -> str:	
		s = ''
		
		if 'n' in format_spec:
			s += " " + self._names
		if 'x' in format_spec:
			s += " " + str(self.xp)
		if ('w') in format_spec:
			s += " " + str(self.weapon.name)
		return (s)	


class Сivilians(Person):
	
	# Класс мирных жителей

	counter = 0 # еще не было создано ни одного жителя

	# Конструктор 	
	def __init__(self, name:str, weapons:Weapon = Stick(), xp:int = 15):
		if (xp < 0):
			raise Game_Error("Xp < 0! :(")
		self.names = name
		self.xp = xp
		self.weapon = weapons
		self.live = True

	#Альтернативный конструктор
	@classmethod
	def standat_pers(cls):
		Сivilians.counter += 1
		return cls("Soldat " + str(Сivilians.counter), Gun())

	# Функция-геттер (делаем его свойством)
	@property
	def names(self):
		return self._names

	# Функция-сеттер
	@names.setter
	def names(self, value):		
		if not isinstance(value, str):
			raise TypeError('Expected a string')
		# Ставим нижнее подчкеркивание чтобы бесконечено не вызывать себя
		self._names = value

	def attack(self, person: Person):
		print(Color.GREEN + self._names + ": I am attack " + person.names + Color.FONE)
		self.weapon.shoot(person)

	def takeDamage(self, weapons: Weapon):
		self.xp = self.xp - weapons.damage
		if (self.xp < 0):
			self.xp = 0
		print(Color.RED)
		print(self.names + ": I am take damge from " + weapons.name)
		print("My xp: " + str(self.xp))
		print(Color.FONE)
		if (self.xp < 0):
			print(Color.RED + self.names + ": I am dead(" + Color.FONE)
			self.live = False



class Hero(Person):
	
	counter = 0 # еще не было создано ни soldata

	# Конструктор 	
	def __init__(self, name:str, weapons: Weapon, armor = 10, xp = 22):
		if (xp < 0):
			raise Game_Error("Xp < 100! :(")
		self.names = name
		self.xp = xp
		self.weapon = weapons
		self.live = True
		self.armor = armor

	#Альтернативный конструктор
	# classmethod спользуется, когда вам нужно получить методы, не относящиеся к какому-либо конкретному экземпляру
	@classmethod
	def standat_pers(cls):
		Hero.counter += 1
		return cls("Soldat " + str(Hero.counter), Automat())

	# Функция-геттер (делаем его свойством)
	@property
	def names(self):
		return self._names

	# Функция-сеттер
	@names.setter
	def names(self, value):		
		if not isinstance(value, str):
			raise TypeError('Expected a string')
		# Ставим нижнее подчкеркивание чтобы бесконечено не вызывать себя
		self._names = value


	def attack(self, person: Person):
		print(Color.GREEN + self._names + ": I am attack " + person.names + Color.FONE)
		self.weapon.shoot(person)

	def takeDamage(self, weapons: Weapon):

		if (self.armor > weapons.damage):
			print(Color.GREEN + self.names + ": The armor worked !" + Color.FONE)
			return
		self.xp = self.xp - (weapons.damage - self.armor)
		if (self.xp <= 0):
			self.xp = 0
		print(Color.RED)
		print(self.names + ": I am take damge from " + weapons.name)
		print("My xp: " + str(self.xp))
		print(Color.FONE)
		if (self.xp <= 0):
			print(Color.RED + self.names + ": I am dead(" + Color.FONE)
			self.live = False


class Enemy(Person):
	
	counter = 0 # еще не было создано ни soldata

	# Конструктор 	
	def __init__(self, name:str, weapons: Weapon, armor = 8, xp = 20):
		if (xp < 0):
			raise Game_Error("Xp < 100! :(")
		self.names = name
		self.xp = xp
		self.weapon = weapons
		self.live = True
		self.armor = armor

	#Альтернативный конструктор
	@classmethod
	def standat_pers(cls):
		Enemy.counter += 1
		return cls("Terrorist " + str(Enemy.counter), Automat_Gun(), 4)

	# Функция-геттер (делаем его свойством)
	@property
	def names(self):
		return self._names

	# Функция-сеттер
	@names.setter
	def names(self, value):		
		if not isinstance(value, str):
			raise TypeError('Expected a string')
		# Ставим нижнее подчкеркивание чтобы бесконечено не вызывать себя
		self._names = value


	def attack(self, person: Person):
		print(Color.GREEN + self._names + ": I am attack " + person.names + Color.FONE)
		self.weapon.shoot(person)

	def takeDamage(self, weapons: Weapon):
		if (self.live == False):
			return
		if (self.armor > weapons.damage):
			print(Color.GREEN + self.names + ": The armor worked !" + Color.FONE)
			return
		self.xp = self.xp - (weapons.damage - self.armor)
		if (self.xp <= 0):
			self.xp = 0
		print(Color.RED)
		print(self.names + ": I am take damge from " + weapons.name)
		print("My xp: " + str(self.xp))
		print(Color.FONE)
		if (self.xp <= 0):
			print(Color.RED + self.names + ": I am dead(" + Color.FONE)
			self.live = False

