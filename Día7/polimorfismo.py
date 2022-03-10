class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'La vaca {self.nombre} hace muuu')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'La oveja {self.nombre} hace muuu')

vaca1 = Vaca('Lola')
oveja1 = Oveja('Cabrita')

#vaca1.hablar()
#oveja1.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)
