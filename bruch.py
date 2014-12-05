__author__ = 'mwech'
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
        else:
            raise TypeError("Zähler und Nenner müssen vom Typ int sein!")

    #Unit_Vergleich
    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return self.zaehler == other.zaehler and self.nenner == other.nenner and isinstance(other, Bruch)

    def __lt__(self, other):
        return float(self.zaehler/self.nenner) < float(other.zaehler/other.nenner)

    def __gt__(self, other):
        return float(self.zaehler/self.nenner) > float(other.zaehler/other.nenner)

    def __ge__(self, other):
        return float(self.zaehler/self.nenner) >= float(other.zaehler/other.nenner)

    def __le__(self, other):
        return float(self.zaehler/self.nenner) <= float(other.zaehler/other.nenner)

    #Unit_Allgemein
    def __float__(self):
        return float(self.zaehler/self.nenner)

    def __int__(self):
        return int(self.zaehler/self.nenner)

    def __str__(self):
        if self.nenner == 1:
            return "(%s)" % abs(self.zaehler)
        else:
            return "(%s/%s)" % (abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        return Bruch(self.zaehler*(-1),self.nenner)

    def __abs__(self):
        return Bruch(abs(self.zaehler),self.nenner)

    def __invert__(self):
        return Bruch(self.nenner, self.zaehler)

    def __complex__(self):
        return complex(self.zaehler)/complex(self.nenner)

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            return Bruch(self.zaehler**power, self.nenner**power)
        else:
            raise TypeError("Wert für pow muss int sein!")

    def _Bruch__makeBruch(param):
        if isinstance(param, int):
            return Bruch(param, 1)
        else:
            raise TypeError("Wert für param muss int sein!")