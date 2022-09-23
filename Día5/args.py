def suma(num1,num2):
    return num1 + num2

print(suma(2,5))

#Usando *args

def suma_con_args(*args):
    total = 0

    for argumento in args:
        total += argumento

    return total

print(suma_con_args(5,7,8,9,5,56))



def suma_absolutos(*args):
    total = 0

    for num in args:
        total += abs(num)
    return total


print(suma_absolutos(-1,3,5,-7))