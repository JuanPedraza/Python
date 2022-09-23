def num_repetidos(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1

    return False

print(num_repetidos(4,6,7,4,0,0,1))
