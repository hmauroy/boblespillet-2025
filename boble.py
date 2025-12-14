"""Klassedefinisjon for Boble"""
from ring import Ring

class Boble(Ring):
    def __init__(self,r,x,y):
        super().__init__(r,x,y)
        self.type = "boble"
        self.levende = True

    def kollisjon(self,objekt2):
        """
        Ved kollisjon med en annen boble (objekt2) skal den største boblen spise den lille. 
        Ny posisjon blir gjennomsnitet av x,y-pos for begge.
        Hvis kollisjon med objekt2 som er en hindring skal boblen sprekke.
        """
        pass
        

    def oppdater(self):
        "Oppdater fart, posisjon, sjekk kollisjon, tegn"
        pass

    
    def areal(self):
        """Returnerer arealet til en boble"""
        pass

    def sprekk_boble(self):
        """
        En form for animasjon viser at boblen sprekker.
        Kanskje blåses opp som flere konsentriske ringer som blir større og større radius 
        mens de første innerste ringene fader ut.
        Kan animeres ved å la ringene vises i x antall frames og for hver y frame opprettes en ny ring.
        """
        pass