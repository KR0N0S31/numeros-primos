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
    
    def is_prime(self):
        for i in range(1, self.num):
            if self.num%i == 0:
                self.iter +=1
            if self.iter > 2:
                return False
        return True

def num_pri(ni, nf):
    iteracion_total = 0
    primos = []
    for i in range(ni, nf):
        print("Analizando el numero: {}".format(i))
        numero = Numero(i)
        if numero.is_prime():
            primos.append(i)
    return primos

def add_list(lst, con, cursor):
    for i in lst:
        read.add_prime_number(i, con, cursor)

def add_base(con, cursor):
    list_prime = num_pri(0,10)
    for i in list_prime:
        read.add_prime_number(i, con, cursor)
