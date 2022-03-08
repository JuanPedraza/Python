class Bird:

    def __init__(self,color, especie):
        self.color = color
        self.especie = especie


my_bird = Bird('Verde','Águila')

print(f'Está ave es un {my_bird.especie} y es de color {my_bird.color}')