lista = ['Hola', 'mundo', 'haciendo', 'pruebas']

archivo = open('texto1.txt','w')

for p in lista:
    archivo.writelines(p + '\n')


archivo.close()