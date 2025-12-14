"""
Ulike funksjoner som er til bruk i animasjonslogikk etc.
main.py skal helst ikke bli noe lengre.
"""

def processKeypress(evt):
    """
    Håndterer tastetrykk.
    """
    key = evt.keysym
    print(f'key: {key}')