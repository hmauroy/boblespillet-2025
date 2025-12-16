""" Klassedefinisjon av Fiende"""
from boble import Boble
from random import random,randrange

class Fiende(Boble):
    """
    Klassen Fiende.
    Driver rundt med tilfeldig fart i 
    en retning i 2-3 sekunder. Så endres farten.
    """
    def __init__(self, r, x, y):
        super().__init__(r, x, y)
        self.type = "fiende"
        self.frameTeller = 0
    
    def oppdater(self):
        """
        Delvis overstyring av superklassens oppdater().
        Skal generere tilfeldig fart og bevegelse.
        """
        self.frameTeller += 1
        if self.frameTeller % 90 == 0:
            self.frameTeller = 0
            self.dx = random() * randrange(True,False)
            self.dy = random() * randrange(True,False)
