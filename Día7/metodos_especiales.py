class Disco:

    def __int__(self,autor, album,canciones):
        self.autor = autor
        self.album = album
        self.canciones = canciones

    def __str__(self):
        return f'El álbum es {self.album} y el autor es {self.autor}'

    def __len__(self):
        return self.canciones

mi_cd = Disco("PINK FLOYD","THE WALL",24)


print(mi_cd)

