""" Klassedefinisjon for Hindring"""

class Hindring:
    """
    Det finnes hindringer i vannet som dukker opp. 
    Disse er kvadratiske og grå for enkelthets skyld.
    Kan være mangekanter hvis ønskelig.
    """
    def __init__(self,a):
        self.type = "hindring"
        pass

    def kollisjon(self,objekt2):
        """
        Hindringer har en annen algorite for å sjekke for kollisjon som ikke 
        benytter Pythagoras som gjelder for kollisjon mellom sirkler (boblene).
        Må se på overlapp av sirkelen og firkanten.
        """
        pass