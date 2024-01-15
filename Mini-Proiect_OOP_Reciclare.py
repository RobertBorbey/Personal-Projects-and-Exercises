# Mini-Proiect OOP : Reciclare

# 1 - Mostenire
class Reciclare:
    def __init__(self, nume_obiect):
        self.nume_obiect = nume_obiect

class Reciclabile(Reciclare):
    def tip(self):
        return "Este reciclabil!"

class Non_reciclabile(Reciclare):
    def tip(self):
        return "Nu este reciclabil!"

carton = Reciclabile(nume_obiect="Carton")
piatra = Non_reciclabile(nume_obiect="Piatra")
print(carton.tip())
print(piatra.tip())

# 2 - Polimorfism

class Hartie:
    def tip_obiect(self):
        return "Acesta este reciclabil!"

class Plastic:
    def tip_obiect(self):
        return "Acesta nu este reciclabil!"

def afiseaza_tip_obiect(recyclable):
    print(recyclable.tip_obiect())

caiet = Hartie()
cauciuc = Plastic()

afiseaza_tip_obiect(caiet)
afiseaza_tip_obiect(cauciuc)

# 3 - Abstractizare

from abc import ABC, abstractmethod

class ReciclareObiecte(ABC):
    @abstractmethod
    def metoda_reciclare(self):
        pass

class Metal(ReciclareObiecte):
    def metoda_reciclare(self):
        print("Implementarea metodei de reciclare")

metal = Metal()
metal.metoda_reciclare()

class SediuReciclare(ABC):
    # @abstractmethod
    # def spalare(self):
    #     raise NotImplementedError

    def verificare(self):
        pass

    @abstractmethod
    def topire(self):
        pass

class SediuReciclare_privat(SediuReciclare):
    nr_obiecte = 0
    adresa = None
    orar = None

    def verificare(self):
        print("Obiectele sunt in curs de verificare")

    def topire(self):
        print("Obiectele sunt in curs de topire")

class SediuReciclare_public(SediuReciclare):
    nr_obiecte = 0
    adresa = None
    orar = None

    def verificare(self):
        print("Obiectele sunt in curs de aprobare")

    def topire(self):
        print("Obiectele sunt in curs de racire")

privat = SediuReciclare_privat()
# privat.spalare()
privat.verificare()
privat.topire()

public = SediuReciclare_public()
public.verificare()
public.topire()

# 4 - Incapsulare

class AgentiaDeReciclare:
    def __init__(self, nume, adresa, capacitate):
        self.nume = nume
        self.adresa = adresa
        self.capacitate = capacitate
        self.tipuriObiecte = []
        self._obiecteReciclabile = 0
        self.__totalReciclate = 100000
        self.faliment = False

    def add_tipObiect(self, tipObiect):
        self.tipuriObiecte.append(tipObiect)

    def remove_tipObiect(self, tipObiect):
        self.tipuriObiecte.remove(tipObiect)

    def recicleaza_obiecte(self, numar_obiecte_reciclate):
        self._obiecteReciclabile += numar_obiecte_reciclate

    @property
    def totalReciclate(self):
        pass

    @totalReciclate.getter
    def totalReciclate(self):
        return self.__totalReciclate

    @totalReciclate.setter
    def totalReciclate(self, modificare_total):
        self.__totalReciclate += modificare_total

    @totalReciclate.deleter
    def totalReciclate(self):
        self.__totalReciclate = 0

agentia_ECO = AgentiaDeReciclare("EcoValue", "Calea Aurel Vlaicu", 5000)
print(f"Tipurile de obiecte care se recicleaza la agentia ECO sunt : {agentia_ECO.tipuriObiecte}")
print(f"Numarul de obiecte reciclabile este : {agentia_ECO._obiecteReciclabile}")
# Apelare GETTER
print(f"Totalul de reciclate accesat prin getter : {agentia_ECO.totalReciclate}")
# Apelare SETTER
agentia_ECO.totalReciclate = 1000
print(f"Totalul de reciclate accesat prin setter : {agentia_ECO.totalReciclate}")
# Apelare Deleter
del agentia_ECO.totalReciclate
print(f"Totalul de reciclate accesat prin deleter : {agentia_ECO.totalReciclate}")