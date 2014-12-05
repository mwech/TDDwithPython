__author__ = 'mwech'
class Bruch():
    zaehler = 1
    nenner = 1

    def __init__(self, zaehler=None, nenner=None):
        if isinstance(zaehler, int) and isinstance(nenner, int):
            self.zaehler = zaehler
            self.nenner = nenner
        if isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner

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

