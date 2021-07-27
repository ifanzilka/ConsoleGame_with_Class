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
			print(Color.GREEN + self.good_team.name_team + " it's win!!! " + Color.FONE)
			return
		self.bad_team.attack(self.good_team)
		if (self.check_win_bad_team()):
			self.live_game = False
			print(Color.GREEN + self.bad_team.name_team + " it's win!!! " + Color.FONE)
			return
		print(self.good_team)
		print(self.bad_team)



try:
	# game = Random_Game("Fcb", "Terror")
	# game.start_game()
	gun = Gun()


	
	gun._recharge()	
	# Как сделать чтобы выше не запускалось

except  BaseException as e:
	print("Error!")
	print(e)


# # Принимает адресс на функциию ниже него
# # def decorate(funct):
# # 	def wrapper(value):
# # 		print("Wrapper")
# # 		funct(value)
# # 	return wrapper	

# # # def decorate2(funct):
# # # 	def wrapper2():
# # # 		print("Wrapper2")
# # # 		funct()
# # # 	return wrapper2	



# # @decorate
# # #@decorate2
# # def test(value):
# # 	print('Test' + value)


# # test1 = decorate(test)

# # #Аналогично
# # test("value")


# #Приходит функция say
# # декортаоры нужны чтобы добавить функционала в функцию
# # def decorator(func):
	
# # 	def inner():
# # 		print("Start decorator")
# # 		func()
# # 		print("End decorator")
# # 	return inner

# # def say():
# # 	print("Hello world")


# # def buy():
# # 	print("Buy world")



# # # d = decorator(say)
# # # print(d)
# # # d() # декоратор + функция декоратора

# # # # Хотим расширить say

# # # say - link in inner
# # say = decorator(say)
# # #print(say)
# # buy = decorator(buy)
# # buy()

# # def decorator(func):
	
# # 	def inner(n, m):
# # 		print("Start decorator")
# # 		func(n, m)
# # 		print("End decorator")
# # 	return inner

# # def say(name, surname):
# # 	print("Hello ", name, surname)

# # def decorator(func):
	
# # 	def inner(*args, **kwargs):
# # 		print("Start decorator")
# # 		func(*args, **kwargs)
# # 		print("End decorator")
# # 	return inner

# # def say(name, surname, age):
# # 	print("Hello ", name, surname, age)



# # def header(func):
	
# # 	def inner(*args, **kwargs):
# # 		print("<h1>")
# # 		func(*args, **kwargs)
# # 		print("</h1>")
# # 	return inner


# # def table(func):
	
# # 	def inner(*args, **kwargs):
# # 		print("<table>")
# # 		func(*args, **kwargs)
# # 		print("</table>")
# # 	return inner

# # def say(name, surname, age):
# # 	print("Hello ", name, surname, age)


# # say = table(header(say))
# # say("vasya", 'ivanov', 30)

# def header(argv):
# 	print("argv_h: " + argv)
# 	def outer(func):

# 		def inner(*args, **kwargs):
# 			print("<" + argv+ ">")
# 			func(*args, **kwargs)
# 			print("</" + argv + ">")
# 		return inner
# 	return outer

# def table(argv):
# 	print("argv_t: " + argv)
# 	def outer(func):
# 	# инициализируем новую функцию
# 		def inner(*args, **kwargs):
# 			print("<"+ argv + ">")
# 			func(*args, **kwargs)
# 			print("</" + argv + ">")
# 		return inner
# 	return outer	



# @table('table')
# @header('h1') #say =  header(say)
# def say(name, surname, age):
# 	print("Hello ", name, surname, age)


# #say = table(header(say))
# say("vasya", 'ivanov', 30)
