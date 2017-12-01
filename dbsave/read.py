import sqlite3
from .config import BASE_DIR

class NumeroQuery(object):
    """docstring for NumeroQuery."""
    def __init__(self, pos, num):
        super(NumeroQuery, self).__init__()
        self.pos = pos
        self.num = num
    
    def __srt__(self):
        return "{}\t|\t{}".format(self.pos, self.num)

def initialize():
    con = sqlite3.connect(BASE_DIR+'/DDBB.sqlite3')
    cursor = con.cursor()

    try:
        cursor.execute(
            """CREATE TABLE numPrimo
                (ID INTEGER PRIMARY KEY NOT NULL,
                NUM INTEGER NOT NULL)"""
                )
    except:
        pass
    con.commit()
    return [con, cursor]

def add_prime_number(num, con, cursor):
    reg = (num,)
    cursor.execute("INSERT INTO numPrimo (NUM) VALUES(?)", reg)
    con.commit()
    print("Numero: {} añadido a la base de datos".format(num))

def last_prime_number(con, cursor):
    cursor.execute("SELECT * FROM numPrimo WHERE ID = (SELECT MAX(ID) FROM numPrimo)")
    prime = [i for i in cursor]
    return prime

def all(con, cursor):
    cursor.execute("SELECT * FROM numPrimo ")
    query = [i for i in cursor]
    return query

def extract(ni, nf, con, cursor):
    query = all(con, cursor)
    nums = []
    for i in query:
        j = NumeroQuery(i[0], i[1])
        if j.num >= ni and j.num <= nf:
            nums.append(j)
    return nums

def close_all(con, cursor):
    con.commit()
    cursor.close()
    con.close()
