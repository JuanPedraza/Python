def prueba(num1,num2,*args,**kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for argumento in args:
        print(f'Argumento es {argumento}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')


# Usando el desempaquetado


args = [10, 20, 30, 40, 50]
kwargs = {
    'x': 'uno',
    'y': 'dos',
    'z': 'tres'
}


prueba(1, 2, *args, **kwargs)

