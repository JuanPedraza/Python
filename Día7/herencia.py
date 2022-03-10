class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Ha acabado de nacer')

class Ave(Animal):
    pass

eagle = Ave(5,'gris')

print(eagle.color)