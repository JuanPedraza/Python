texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

nuevo_texto = texto.lstrip(',:_#')
print(nuevo_texto)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(4,"naranja")

print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

a = marcas_smartphones.isdisjoint(marcas_tv)
print(a)