def contar_primos(num):
    primos = [2]
    iterable = 3

    if num < 2:
        return 0

    while iterable <= num:
        for n in range(3,iterable,2):
            if iterable % n == 0:
                iterable += 2
                break
        else:
            primos.append(iterable)
            iterable += 2
    print(primos)
    return len(primos)

print(contar_primos(60))