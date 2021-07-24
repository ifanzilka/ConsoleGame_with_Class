from Color import *

class Game_Error(Exception):
    def __init__(self, text):
        tmp = RED + text + FONE
        self.txt = tmp
    def __str__(self):
        return self.txt
