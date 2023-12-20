import math
from dolgozo import Dolgozo

class Ber:
    #Konstruktor - az osztályváltozóknak kezdő értéket adunk
    def __init__(self):
        self.filename = 'berkft.txt'
        self.dolgozo_lista = []

    #Fájl beolvasása
    def olvas_fajl(self):
        fp = open(self.filename, 'r', encoding='UTF-8')
        lines = fp.readlines()
        fp.close()
        for line in lines:
            line = line.rstrip()
            (nev, telepules, cim, szuletes, fizetes) = line.split(':')
            dolgozo = Dolgozo(nev, telepules, cim, szuletes, fizetes)
            self.dolgozo_lista.append(dolgozo)

    #Szolnokiak
    def szolnoki(self):
        szolnoki_lista = []
        for dolgozo in self.dolgozo_lista:
            if dolgozo.telepules == 'Szolnok':
                szolnoki_lista.append(dolgozo)
        max_szolnoki = szolnoki_lista[0]
        for szolnoki in szolnoki_lista:
            if szolnoki.szuletes > max_szolnoki.szuletes:
                max_szolnoki = szolnoki
        print(max_szolnoki.szuletes)

    def hatvani_fizetes(self):
        osszeg = 0
        for dolgozo in self.dolgozo_lista:
            if dolgozo.telepules == 'Hatvan':
                osszeg += int(dolgozo.fizetes)
        print(osszeg)

ber = Ber()
ber.olvas_fajl()
ber.szolnoki()
ber.hatvani_fizetes()