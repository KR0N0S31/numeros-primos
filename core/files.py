def save_user_numbers(lst):
    with open('result.txt', 'w') as f:
        f.write("Posición\t|\tNumero \n")
        for l in lst:
            f.write("{}\t|\t{} \n".format(l.pos, l.num))
