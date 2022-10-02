mi_lista = [1,1,1,1,1,1,1]
print(len(mi_lista))

class Objeto:
    pass

mi_objeto = Objeto()
print((mi_objeto))
#print(len(mi_objeto))  da error porque objeto no tiene largo


class CD:
    def __init__(self,autor, titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return(f'album: {self.titulo} de {self.autor}')

    def __len__(self):
        return self.canciones
        
mi_cd = CD('pink floyd', 'the wall', 24)
print(str(mi_cd))
print(len(mi_cd))

