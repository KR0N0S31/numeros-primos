from core import primos, interface, files
from dbsave import read, config


if __name__ == '__main__':
    print("Numeros primos, version {}".format(config.VERSION))
    dbinfo = read.initialize()
    con = dbinfo[0]
    cursor = dbinfo[1]
    last_prime = read.last_prime_number(con, cursor)
    if not last_prime:
        primos.add_base(con, cursor)
    last_prime = read.last_prime_number(con, cursor)[0]
    
    ni, nf = interface.input_val()
    while True:
        if not ni and not nf:
            print("Los numeros son iguales, porfavor ingrese entradas validas.")
            ni, nf = interface.input_val()
        else:
            break
    if nf > last_prime[1]:
        primos_sin_añadir = primos.num_pri(last_prime[1], nf)
        primos.add_list(primos_sin_añadir, con, cursor)
    query = read.extract(ni, nf, con, cursor)
    total = len(read.all(con, cursor))
    files.save_user_numbers(query)
    print("En el rango de {} a {}, hay {} numeros primos, estos se guardaran en el archivo result.txt".format(ni, nf, len(query)))
    print("En total hay {} numeros primos en la base de datos.".format(total))
    read.close_all(con, cursor)
