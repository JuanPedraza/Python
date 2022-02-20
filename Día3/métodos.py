"""
Métodos más usados en los strings

upper() ---> Pasar a mayúsculas
lower() ---> Pasar a minúsculas
split() ---> Separarlos en partes(lista)
join() ---> Unir ítems usando separador
find() ---> Encontrar un sub-string
replace() ---> Reemplazar un sub-string
"""
a = "Python"
b= "es"
c = "cool"
texto = "Madrid es la capital de España"

resultado = texto.upper()
print(resultado)
resultado = texto.lower()
print(resultado)
resultado = texto.split()
print(resultado)
resultado = " ".join([a,b,c])
print(resultado)
resultado = texto.replace("Madrid", "Barcelona")

print(resultado)