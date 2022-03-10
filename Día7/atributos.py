class Bird:

    #Atributos de clase
    alas = True

    #Atributos de instancia
    def __init__(self,color, especie):
        self.color = color
        self.especie = especie

    #Métodos de instancia
    def sound(self):
        print(f'El pájaro hace algún sonido y es de color {self.color}')

    def volar(self,metros):
        print(f'El ave voló {metros} metros')
        #Método de instancia
        self.sound()
    #Método de clase - No tengo que instanciar la clase para acceder al método con el decorador @Classmethod
    @classmethod

    def poner_huevos(cls,cantidad):
        print(f'El ave puso {cantidad} huevos')

    @staticmethod

    def correr():
        print('El pájaro corre')





#my_bird = Bird('Verde','Águila')


#Bird.volar(90)

Bird.poner_huevos(9)
Bird.correr()