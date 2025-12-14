""" Klassedefinisjon av Fiende"""
from boble import Boble

class Fiende(Boble):
    def __init__(self, r, x, y):
        super().__init__(r, x, y)
        self.type = "fiende"
    
    def oppdater(self):
        """
        Delvis overstyring av superklassens oppdater().
        Skal generere tilfeldig fart og bevegelse.
        """
        pass