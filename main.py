from Populacja import *
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ILE_WYN = 40 # uruchomienia programu

PR_KRZYZ = 80 #[%] prawdopodobieństwo krzyżowania
PR_MUT = 10    #[%] prawdopodobieństwo mutacji

ILE_OS = 18   # ilość osobników
LB_POP = 8   # liczba populacji


def f(x, A = 4, B = 7, C = 2):
    return A * x * x + B * x + C

with open('wyniki.txt', 'w') as file:
    for c in range(ILE_WYN):
        populacja = Populacja(ILE_OS, PR_KRZYZ, PR_MUT, f)

        while populacja.generacja < LB_POP:
            populacja.laczenie_w_pary()
            populacja.krzyzowanie()
            populacja.mutacja()
            populacja.selekcja()
            populacja.nastepna_generacja()

        najlepszy = {
            'fx' : populacja.najlepszy_osobnik[0],
            'x'  : populacja.najlepszy_osobnik[1]
        }
        wynik = f'{najlepszy["fx"]} {najlepszy["x"]}'


        file.write(wynik+'\n')
        
        if najlepszy["x"] == 255:
            print(f'{bcolors.OKGREEN}{wynik}{bcolors.ENDC}')

        elif najlepszy["x"] in range(250, 255):
            print(f'{bcolors.WARNING}{wynik}{bcolors.ENDC}')

        else:
            print(f'{bcolors.FAIL}{wynik}{bcolors.ENDC}')

