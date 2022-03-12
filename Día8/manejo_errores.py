def suma():
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))
    print(num1 + num2)
    print('Gracias por sumar los números')

try:
    suma()
except:
    print('Algo ha salido mal')
finally:
    print('Hasta pronto')