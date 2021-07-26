from Color import Color

class Game_Error(Exception):
    def __init__(self, text):
        tmp = Color.RED + text + Color.FONE
        self.txt = tmp
    def __str__(self):
        return self.txt
