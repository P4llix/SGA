import random

class Osobnik:
    def __init__(self, ciag = ''):
        if not ciag:
            self.ciag = [str(random.randint(0, 1)) for _ in range(8)]
        else:
            self.ciag = list(ciag)

    def __str__(self):
        return ''.join(self.ciag)

    def __int__(self):
        return int(''.join(self.ciag), 2)

    def mutuj(self, gen):
        if self.ciag[gen] == '0':
            self.ciag[gen] = '1'
        else:
            self.ciag[gen] = '0'