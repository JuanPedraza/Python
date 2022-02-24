num1 = int(input("Escriba un número: "))
num2 = int(input("Escriba otro número: "))
def suma(num1,num2):
    resultado = num1 + num2
    return  resultado

print(suma(num1,num2))


palabra = 'python'
def invertir_palabra(palabra):
    resultado = palabra.upper()[::-1]
    return resultado

print(invertir_palabra(palabra))