from Color import Color
import sys

class Game_Error(Exception):
	def __init__(self, text):
		tmp = Color.RED + text + Color.FONE
		self.txt = tmp
	
	def __str__(self):
		return self.txt

def change_fd(argv):
	def outer(func):
		def inner(*args, **kwargs):
			tmp = sys.stdout
			sys.stdout = sys.stderr
			func(*args, **kwargs)
			sys.stdout = tmp
		# File with fun
		inner.__module__ = func.__module__
		
		# name fun
		inner.__name__ = func.__name__
		
		# Coments
		inner.__doc__ = func.__doc__
		
		# if (gv.change_fd_err == True):
		# 	print("ok")
		# 	return inner
		# else:
		# 	print("ko")
		# 	return func
		return inner

	return outer	

@change_fd('')
def	print_err(e):
	"""Add RED Color From write txt :)"""
	print(Color.RED,end='')
	print(e)
	print(Color.FONE,end= '')