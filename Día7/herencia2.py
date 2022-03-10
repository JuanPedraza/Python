#Herencia múltiple

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('jajajajaja')

class Hijo(Padre,Madre):
    def saltar(self):
        print('Todos saltan')

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()
mi_nieto.saltar()