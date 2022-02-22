pies = [10,20,30]

metros = [p * 3.281 for p in pies]

print(metros)


valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [valor for valor in valores if valor % 2 == 0 ]

print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [((temperatura-32)*(5/9)) for temperatura in temperatura_fahrenheit]