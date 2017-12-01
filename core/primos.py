import sys
from dbsave import read

class Numero(object):
    """docstring for Numero."""
    def __init__(self, num):
        super(Numero, self).__init__()
        self.num = num
        self.iter = 0

    def add_iter(self):
        self.iter += 1

def num_pri(ni, nf):
    iteracion_total = 0
    primos = []
    for i in range(nf, ni, -1):
        print("Analizando el numero: {}".format(i))
        numero = Numero(i)
        for j in range(1, i):
            pri = i/j
            iteracion_total += 1
            if pri == int(pri):
                numero.add_iter()
                if numero.iter >= 2:
                    break
        if numero.iter == 1:
            primos.append(i)
    primos.reverse()
    return primos

def add_list(lst, con, cursor):
    for i in lst:
        read.add_prime_number(i, con, cursor)

def add_base(con, cursor):
    list_prime = num_pri(0,10)
    for i in list_prime:
        read.add_prime_number(i, con, cursor)
