__author__ = 'mwech'
from operator import *

class Bruch():
    zaehler = 1
    nenner = 1

    def __init__(self, zaehler=None, nenner=None):
        if isinstance(zaehler, int) and isinstance(nenner, int):
            if nenner != 0:
                self.zaehler = zaehler
                self.nenner = nenner
            else:
                raise ZeroDivisionError("Nenner darf nicht 0 sein!")
        elif isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
        elif isinstance(zaehler, int) and not isinstance(nenner, float):
            self.zaehler = zaehler
            self.nenner = 1
        else:
            raise TypeError("Zähler und Nenner müssen vom Typ int sein!")

    # Unit_Vergleich
    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return self.zaehler == other.zaehler and self.nenner == other.nenner and isinstance(other, Bruch)

    def __lt__(self, other):
        return float(self.zaehler / self.nenner) < float(other.zaehler / other.nenner)

    def __gt__(self, other):
        return float(self.zaehler / self.nenner) > float(other.zaehler / other.nenner)

    def __ge__(self, other):
        return float(self.zaehler / self.nenner) >= float(other.zaehler / other.nenner)

    def __le__(self, other):
        return float(self.zaehler / self.nenner) <= float(other.zaehler / other.nenner)

    #Unit_Allgemein
    def __float__(self):
        return float(self.zaehler / self.nenner)

    def __int__(self):
        return int(self.zaehler / self.nenner)

    def __str__(self):
        z = abs(self.zaehler)
        n = abs(self.nenner)
        if self.nenner == 1:
            return "(%s)" % z
        elif self.nenner != 1:
            return "(%s/%s)" % (z, n)

    def __neg__(self):
        return Bruch(self.zaehler * (-1), self.nenner)

    def __abs__(self):
        return Bruch(abs(self.zaehler), self.nenner)

    def __invert__(self):
        return Bruch(self.nenner, self.zaehler)

    def __complex__(self):
        return complex(self.zaehler) / complex(self.nenner)

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError("Wert für pow muss int sein!")

    def _Bruch__makeBruch(param):
        if isinstance(param, int):
            return Bruch(param, 1)
        else:
            raise TypeError("Wert für param muss int sein!")

    #Unit_Addition
    def __add__(self, other):
        if isinstance(self, Bruch) and isinstance(other, Bruch):
            return float(self.zaehler / self.nenner) + float(other.zaehler / other.nenner)
        elif isinstance(self, Bruch) and isinstance(other, int):
            return float(self.zaehler / self.nenner) + other
        else:
            raise TypeError("Nur int als Summanden erlaubt!")

    def __radd__(self, other):
        return float(self) + float(other)

    def __iadd__(self, other):
        if isinstance(other, int):
            wert = other * self.nenner
            return Bruch(iadd(self.zaehler, wert), self.nenner)
        elif isinstance(other, Bruch):
            return Bruch(iadd(self.zaehler, other.zaehler * self.nenner), self.nenner)
        else:
            raise TypeError("Nur int oder Bruch als Summand erlaubt!")