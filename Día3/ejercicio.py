texto = input("Escribe un texto: ").lower()
letras = input("Escriba tres letras de su preferencia: ").lower()

lista_letras = letras.split()

print(lista_letras)

print(f'La letra {lista_letras[0]} se repite en el texto {texto.count(lista_letras[0])} veces')

total_palabras = texto.split()

print(f'El texto tiene {len(total_palabras)} palabras en total')

letra_inicio = texto[0]
letra_final = texto[-1]
print(f'La primer letra del texto es {letra_inicio} y la última es {letra_final}')

total_palabras.reverse()
texto_invertido = ' '.join(total_palabras)

print(f'Mi texto invertido queda así: {texto_invertido}')

palabra_python = 'python' in texto
dic_python = {True: "Si", False: "No"}

print(f'La palabra "Python" {dic_python[palabra_python]} se encuentra en el texto')

