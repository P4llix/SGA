from Osobnik import *

class Populacja:
    def __init__(self, ile_os, pr_krzyz, pr_mut, f):
        self.funkcja = f
        self.pr_krzyz = pr_krzyz
        self.pr_mut = pr_mut
        self.ile_os = ile_os
        self.populacja = [Osobnik() for _ in range(ile_os)]
        self.suma = 0
        self.generacja = 0
        self.najlepszy_osobnik = (0, None)
        self.roznica = 0


    def laczenie_w_pary(self):
        self.pary = [
                (self.populacja[i], self.populacja[i+1])
                for i in range(0, len(self.populacja), 2)
            ]


    def prawdopodobiestwo(self, czego):
        if random.randint(1, 100) <= czego:
            return True
        else:
            return False


    def krzyzowanie(self):
        populacja_tymczasowa = []
        for para in self.pary:
            rodzic1, rodzic2 = para[0], para[1]
            czy_krzyzuje = self.prawdopodobiestwo(self.pr_krzyz)

            if not czy_krzyzuje: 
                populacja_tymczasowa.append(rodzic1)
                populacja_tymczasowa.append(rodzic2)
                continue

            pc = random.randint(1, 7)

            dziecko1 = Osobnik(str(rodzic1)[0 : pc] + str(rodzic2)[pc :: ])
            dziecko2 = Osobnik(str(rodzic2)[0 : pc] + str(rodzic1)[pc :: ])

            populacja_tymczasowa.append(dziecko1)
            populacja_tymczasowa.append(dziecko2)

        self.populacja = populacja_tymczasowa

    def mutacja(self):
        for osobnik in self.populacja:
            for index in range(0, len(str(osobnik))):

                czy_mutuje = self.prawdopodobiestwo(self.pr_mut)
                if czy_mutuje: 
                    osobnik.mutuj(index)


    def suma_populacji(self):
        self.suma = sum([self.funkcja(int(osobnik)) for osobnik in self.populacja])


    def sprawdzanie_ujemnych(self):
        wartosci_osobnikow = [int(osobnik) for osobnik in self.populacja]
        if min(wartosci_osobnikow) < 0:
            self.roznica = min(wartosci_osobnikow)


    def selekcja(self):
        self.suma_populacji()
        self.sprawdzanie_ujemnych()

        wagi = [] # prawdopodobienstwo wylosowania osobnika
        osobniki = [] # lista wartosci osobnikow

        for osobnik in self.populacja:
            wagi.append((self.funkcja(int(osobnik))/self.suma)+self.roznica)
            osobniki.append(int(osobnik))

        populacja_tymczasowa = []
        for _ in range(len(self.populacja)):
            potomek = random.choices(osobniki, wagi)[0]
            populacja_tymczasowa.append(Osobnik(format(potomek, '08b')))
        self.populacja = populacja_tymczasowa

        self.suma_populacji()

        for osobnik in self.populacja:
            wartosc_osobnika = self.funkcja(int(osobnik))

            if wartosc_osobnika > self.najlepszy_osobnik[0]:
                self.najlepszy_osobnik = (wartosc_osobnika, int(osobnik))


    def nastepna_generacja(self):
        self.generacja += 1
