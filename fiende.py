""" Klassedefinisjon av Fiende"""
from boble import Boble
from random import random,randrange

class Fiende(Boble):
    """
    Klassen Fiende.
    Driver rundt med tilfeldig fart i 
    en retning i 2-3 sekunder. Så endres farten.
    """
    def __init__(self, r, x, y, id):
        super().__init__(r, x, y, 0, id)
        self.type = "fiende"
        self.frameTeller = 0
    
    def oppdater_helper(self):
        """
        Overstyring av superklassens oppdater_helper().
        Skal generere tilfeldig fart og bevegelse.
        Bør egentlig gå mot helten aktivt.
        """
        self.frameTeller += 1
        if self.frameTeller % 90 == 0:
            self.frameTeller = 0
            self.dx = 100/self.R * random() * randrange(-2,2)
            self.dy = 100/self.R * random() * randrange(-2,2)
            print(self.dx)
            print(self.dy)
        self.x += self.dx
        self.y += self.dy
        if self.y + self.R < 0:
            self.levende = False
    