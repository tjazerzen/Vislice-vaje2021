import random

# Najprej konstante

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"

ZMAGA = "W"
PORAZ = "X"

class Igra:

    def __init__(self, geslo, crke=""):
        self.geslo = geslo.upper()
        self.crke = crke.upper()

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all([i in self.crke for i in self.geslo])

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        rezultat = ""
        for char in self.geslo:
            if char not in self.crke:
                rezultat += "_"
            else:
                rezultat += char
        return rezultat

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if self.poraz():
            return PORAZ
        if crka in self.crke:
            return PONOVLJENA_CRKA
        self.crke += crka
        if self.zmaga():
            return ZMAGA
        if crka in self.geslo:
            return PRAVILNA_CRKA
        if self.poraz():
            return PORAZ
        return NAPACNA_CRKA


bazen_besed = []
with open("nabor_besed.txt", encoding="utf8") as input_file:
    bazen_besed = [i.strip() for i in input_file.readlines()]


def nova_igra(bazen_besed):
    beseda = random.choice(bazen_besed)
    return Igra(beseda)