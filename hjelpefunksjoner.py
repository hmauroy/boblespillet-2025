"""
Ulike funksjoner som er til bruk i animasjonslogikk etc.
main.py skal helst ikke bli noe lengre.
"""

def processKeypress(evt,helt):
    """
    Håndterer tastetrykk for Helt-objektet.
    """
    key = evt.keysym
    #print(f'key: {key}')
    if key == "Up":
        dx = 0
        dy = -1
    elif key == "Right":
        dx = 1
        dy = 0
    elif key == "Down":
        dx = 0
        dy = 1
    elif key == "Left":
        dx = -1
        dy = 0
    helt.sett_ny_fart(dx,dy)

def processKeyRelease(evt,helt):
    """
    Oppdaterer dx og dy for helten så den står stille.
    """
    #print("Key RELEASE!")
    helt.sett_ny_fart(0,0)

def showEndScreen():
    str1 = ""
    for i in range(20):
        str1 += "*"
    str2 =  str1 + "   GAME OVER!   " + str1
    print(str2)
    

