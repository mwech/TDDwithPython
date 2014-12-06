"""
Created on 02.12.2014
Finished Implementation on 06.12.2014

@author: mwech
@version: 20141206
@description: Klasse zur Implementierung einiger Operationen, um das Rechnen mit Brüchen zu ermöglichen.
"""
__author__ = 'mwech'
from operator import *

class Bruch():
    def __init__(self, zaehler=None, nenner=None):
        """
        Konstruktor
        :type zaehler: Zähler des Bruchs
        :type nenner: Zähler des Nenners
        """
        if isinstance(zaehler, int) and isinstance(nenner, int):
            #Wenn Zähler und Nenner vom Datentyp Integer sind
            if nenner != 0:
            #Überprüfen ob der nenner 0 ist --> Division durch 0 ist nicht erlaubt
                self.zaehler = zaehler
                self.nenner = nenner
            else:
            #Exceptionhandling da Zähler 0 ist, und dadurch die Divsion nicht möglich ist
                raise ZeroDivisionError("Nenner darf nicht 0 sein!")

        elif isinstance(zaehler, Bruch):
            #Für den Fall, dass der Zähler vom Typ Bruch ist, z.B.: self.b2 = Bruch(self.b)
            #Zuweisen von Zähler und Nenner aus dem Bruchobjekt
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner

        elif isinstance(zaehler, int) and not isinstance(nenner, float):
            #Für den Fall, dass die Klasse folgendermaßen aufgerufen wird: Bruch(4)
            # --> ohne Nenner, daher Deklarierung von Nenner = 1
            self.zaehler = zaehler
            self.nenner = 1
        else:
            raise TypeError("Zähler und/oder Nenner nicht zulässig!")

    # Unit_Vergleich
    def __ne__(self, other):
        """
        Überschreiben (Neu definieren) der != Methode; --> Funktion von != deklarieren
        :type self: Bruch1
        :type other: Bruch2
        """
        return not self.__eq__(other)

    def __eq__(self, other):
        """
        Überschreiben  (Neu definieren) der == Methode; --> Funktion von == deklarieren
        :type self: Bruch1
        :type other: Bruch2
        """
        return self.zaehler == other.zaehler and self.nenner == other.nenner and isinstance(other, Bruch)

    def __lt__(self, other):
        """
        Überschreiben (Neu definieren) der < (kleiner) Methode; --> Funktion von < deklarieren
        :type self: Bruch1
        :type other: Bruch2
        """
        return float(self.zaehler / self.nenner) < float(other.zaehler / other.nenner)

    def __gt__(self, other):
        """
        Überschreiben (Neu definieren) der > (kleiner) Methode; --> Funktion von > deklarieren
        :type self: Bruch1
        :type other: Bruch2
        """
        return float(self.zaehler / self.nenner) > float(other.zaehler / other.nenner)

    def __ge__(self, other):
        """
        Überschreiben (Neu definieren) der >= (kleiner) Methode; --> Funktion von >= deklarieren
        :type self: Bruch1
        :type other: Bruch2
        """
        return float(self.zaehler / self.nenner) >= float(other.zaehler / other.nenner)

    def __le__(self, other):
        """
        Überschreiben (Neu definieren) der <= (kleiner) Methode; --> Funktion von <= deklarieren
        :type self: Bruch1
        :type other: Bruch2
        """
        return float(self.zaehler / self.nenner) <= float(other.zaehler / other.nenner)

    # Unit_Allgemein
    def __float__(self):
        """
        Überschreiben der Methode um einen Bruch in einen float Wert umzuwandeln
        :type self: Bruch
        """
        return float(self.zaehler / self.nenner)

    def __int__(self):
        """
        Überschreiben der Methode um einen Bruch in einen Integer Wert umzuwandeln
        :type self: Bruch
        """
        return int(self.zaehler / self.nenner)

    def __str__(self):
        """
        Überschreiben der Methode um einen Bruch in ein String Objekt umzuwandeln
        :type self: Bruch
        """
        #Zähler und Nenner durch abs() positiv machen
        z = abs(self.zaehler)
        n = abs(self.nenner)
        #Für den Fall, dass der Nenner 1 ist, muss nur der Zähler als String return werden
        if self.nenner == 1:
            return "(%s)" % z
        elif self.nenner != 1:
        #Zähler und Nenner als String returnen
            return "(%s/%s)" % (z, n)

    def __neg__(self):
        """
        Überschreiben der Methode um das Vorzeichen des Bruchs zu ändern; nur für den Zähler notwendig
        :type self: Bruch
        """
        return Bruch(self.zaehler * (-1), self.nenner)

    def __abs__(self):
        """
        Überschreiben der Methode um den Betrag zu bestimmen-> Vorzeichen positiv machen, nur für den Zähler notwendig
        :type self: Bruch
        """
        return Bruch(abs(self.zaehler), self.nenner)

    def __invert__(self):
        """
        Überschreiben der Methode um Zähler und Nenner zu vertauschen, invertieren
        :type self: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __complex__(self):
        """
        Überschreiben der Methode um Zähler und Nenner komplex zu machen
        :type self: Bruch
        """
        return complex(self.zaehler) / complex(self.nenner)

    def __pow__(self, power, modulo=None):
        """
        Überschreiben der Methode um den Bruch zu potenzieren
        :type self: Bruch
        :type power: zu potenzierender Wert
        """
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError("Wert für pow muss int sein!")

    def _Bruch__makeBruch(param):
        """
        Methode, die einen integer Wert in einen Bruch (Nenner 1) umwandelt.
        :type self: Bruch
        :type power: zu potenzierender Wert
        """
        if isinstance(param, int):
            return Bruch(param, 1)
        else:
            raise TypeError("Wert für param muss int sein!")

    #Unit_Addition
    def __add__(self, other):
        """
        Überschreiben der Methode um Brüche zu addieren
        :type self: Bruch
        :type other: Bruch2, oder Integer Wert
        """
        if isinstance(self, Bruch) and isinstance(other, Bruch):
            return float(self.zaehler / self.nenner) + float(other.zaehler / other.nenner)
        elif isinstance(self, Bruch) and isinstance(other, int):
            return float(self.zaehler / self.nenner) + other
        else:
            raise TypeError("Nur int als Summanden erlaubt!")

    def __radd__(self, other):
        """
        Überschreiben der Methode um das Addieren mit vertauschten Operanden zu ermöglichen
        :type self: Bruch
        :type other: Integer Wert
        """
        return float(self) + float(other)

    def __iadd__(self, other):
        """
        Überschreiben der Methode um die Operation += ausführen zu können
        :type self: Bruch
        :type other: Bruch2 / Integer Wert
        """
        if isinstance(other, int):
            wert = other * self.nenner
            return Bruch(iadd(self.zaehler, wert), self.nenner)
        elif isinstance(other, Bruch):
            return Bruch(iadd(self.zaehler, other.zaehler * self.nenner), self.nenner)
        else:
            raise TypeError("Nur int oder Bruch als Summand erlaubt!")

    #Unit Subtraktion
    def __sub__(self, other):
        """
        Überschreiben der Methode um Brüche zu subtrahieren
        :type self: Bruch
        :type other: Bruch2, oder Integer Wert
        """
        if isinstance(self, Bruch) and isinstance(other, Bruch):
            return float(self.zaehler / self.nenner) - float(other.zaehler / other.nenner)
        elif isinstance(self, Bruch) and isinstance(other, int):
            return float(self.zaehler / self.nenner) - other
        else:
            raise TypeError("Nur int als zu subtrahierender Wert erlaubt!")

    def __rsub__(self, other):
        """
        Überschreiben der Methode um das Subtrahieren mit vertauschten Operanden zu ermöglichen
        :type self: Bruch
        :type other: Integer Wert
        """
        if isinstance(other, int):
            return other - self.zaehler / self.nenner
        else:
            raise TypeError("Nur int als Wert erlaubt!")

    def __isub__(self, other):
        """
        Überschreiben der Methode um die Operation -= ausführen zu können
        :type self: Bruch
        :type other: Bruch2 / Integer Wert
        """
        if isinstance(other, int):
            return Bruch(isub(self.zaehler, other * self.nenner), self.nenner)
        elif isinstance(other, Bruch):
            return Bruch(isub(self.zaehler, other.zaehler * self.nenner), self.nenner)
        else:
            raise TypeError("Nur int als Wert erlaubt!")

    #Unit Multiplikation
    def __mul__(self, other):
        """
        Überschreiben der Methode um Brüche zu multiplizieren
        :type self: Bruch
        :type other: Bruch2, oder Integer Wert
        """
        if isinstance(self, Bruch) and isinstance(other, Bruch):
            return float(self.zaehler / self.nenner) * float(other.zaehler / other.nenner)
        elif isinstance(self, Bruch) and isinstance(other, int):
            return float(self.zaehler / self.nenner) * other
        else:
            raise TypeError("Nur int als zu multiplizierender Wert erlaubt!")

    def __rmul__(self, other):
        """
        Überschreiben der Methode um das Subtrahieren mit vertauschten Operanden zu ermöglichen
        :type self: Bruch
        :type other: Integer Wert
        """
        return self.zaehler * other / self.nenner

    def __imul__(self, other):
        """
        Überschreiben der Methode um die Operation *= ausführen zu können
        :type self: Bruch
        :type other: Bruch2 / Integer Wert
        """
        if isinstance(other, int):
            return imul(self.zaehler, other) / self.nenner
        elif isinstance(other, Bruch):
            return imul(self.zaehler, other.zaehler) / self.nenner
        else:
            raise TypeError("Nur int als Wert erlaubt!")

    #Unit Division --> truediv, weil __div__ veraltet und in Python3 nicht mehr verfügbar ist
    def __truediv__(self, other):
        """
        Überschreiben der Methode um Brüche zu dividieren
        :type self: Bruch
        :type other: Bruch2, oder Integer Wert
        """
        if isinstance(self, Bruch) and isinstance(other, Bruch):
            return float(self.zaehler / self.nenner) / float(other.zaehler / other.nenner)
        elif isinstance(self, Bruch) and isinstance(other, int):
            return float(self.zaehler / self.nenner) / other
        elif isinstance(self, Bruch) and other == 0:
            raise ZeroDivisionError("Division durch 0 nicht erlaubt!")
        else:
            raise TypeError("Nur int als zu dividierender Wert erlaubt!")

    def __rtruediv__(self, other):
        """
        Überschreiben der Methode um das Dividieren mit vertauschten Operanden zu ermöglichen
        :type self: Bruch
        :type other: Integer Wert
        """
        if isinstance(other, int) and isinstance(self, Bruch):
            return other / (self.zaehler / self.nenner)
        if other == 0:
            raise ZeroDivisionError("Division durch 0 nicht erlaubt!")
        if not isinstance(other, int) and isinstance(self, Bruch):
            raise TypeError("Nur int als  Wert erlaubt!")

    def __itruediv__(self, other):
        """
        Überschreiben der Methode um die Operation /= ausführen zu können
        :type self: Bruch
        :type other: Bruch2 / Integer Wert
        """
        if isinstance(other, int):
            return Bruch(self.zaehler, self.nenner * other)
        elif isinstance(other, Bruch):
            return Bruch(self.zaehler, self.nenner * other.zaehler)
        else:
            raise TypeError("Nur int als Wert erlaubt!")

    #Unit Zusatz
    def __iter__(self):
        """
        Methode, um Iterator Objekte zurückzuliefern
        :type self: object
        """
        #1.Wert --> Zähler, yield statt return
        yield self.zaehler
        #2.Wert --> Nenner, yield statt return
        yield self.nenner
