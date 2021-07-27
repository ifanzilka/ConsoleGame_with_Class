from Color import Color
import sys

def change_fd(argv):
	def outer(func):
		def inner(*args, **kwargs):
			tmp = sys.stdout
			sys.stdout = sys.stderr
			func(*args, **kwargs)
			sys.stdout = tmp
		return inner
	return outer	

@change_fd('')
def	print_err(e):
	print(Color.RED)
	print(e)
	print(Color.FONE)

class Game_Error(Exception):
    def __init__(self, text):
        tmp = Color.RED + text + Color.FONE
        self.txt = tmp

    def __str__(self):
        return self.txt
