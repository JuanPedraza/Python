registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open('registro.txt', 'a')

for r in registro_ultima_sesion:
    archivo.writelines(r + '\t')

archivo.close()

archivo = open('registro.txt', 'r')
print(archivo.read())
archivo.close()