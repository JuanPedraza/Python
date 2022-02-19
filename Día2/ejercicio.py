"""Pedir nombre, pedir ingreso en ventas y calcylar las ganancias"""

name = input("¿Cuál es tu nombre?: ")
sales = float(input("Escribe el valor de tus ventas: "))
porcentaje = 13
total_ventas = round(sales*porcentaje/100,2)

print(f"Hola {name} el total de tus ganancias son de {total_ventas}")