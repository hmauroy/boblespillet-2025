"""Klassedefinisjon for Helt"""
from boble import Boble

class Helt(Boble):
    def __init__(self, r, x, y, id):
        super().__init__(r, x, y, 0, id)
        self.type = "helt"
        self.poeng = 0
        self.dy = 0
        self.fart = None
    
    def sett_ny_fart(self,dx,dy):
        self.dx = dx * 100/self.R
        self.dy = dy * 100/self.R

    def oppdater_helper(self):
        """Override av Boble.oppdater()."""
        self.x += self.dx
        self.y += self.dy
        self.merge = False

    def kollisjon(self, objekt2):
        """
        Hvis helten treffer en annen boble skal den spise den andre hvis mindre.
        Ellers dør helten.
        """
        super().kollisjon(objekt2)