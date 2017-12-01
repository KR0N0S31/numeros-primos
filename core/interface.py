def valid_input(str_inp, default):
    inp = input(str_inp)
    while True:
        if inp == 'q':
            sys.exit(1)
        if inp == '':
            return default
        try:
            num = int(inp)
            if num >= 0:
                return num
            elif num < 0:
                inp = input("Entrada no valida 1: ")
        except:
            inp = input("Entrada no valida 2: ")

def order(a, b):
    if a == b:
        return False, False
    elif a > b:
        nMa = a
        nMi = b
    elif a < b:
        nMa = b
        nMi = a
    return nMi, nMa

def input_val():
    print("Pulsar 'q' para salir")
    print("Ingrese un numero para mostrarle los numeros primos menores y/o iguales a ese numero")
    ni = valid_input("Si desea el valor por defecto(0), deje en blanco: ", 0)
    print("Pulsar 'q' para salir")
    print("Ingrese un numero para mostrarle los numeros primos mayores y/o iguales a ese numero")
    nf = valid_input("Si desea el valor por defecto(100), deje en blanco: ", 100)
    ni, nf = order(ni, nf)
    return ni, nf