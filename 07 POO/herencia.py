class Animal:

    def __init__(self,edad,color) :
        self.edad=edad
        self.color= color
        pass
    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite sonido')


class Pajaro(Animal):

    def __init__(self, edad, color,altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo=altura_vuelo
    def hablar(self):
        print('pio')

    def volar(self, metros):
        print(f'voló {metros}')


print(Animal.__subclasses__())
piolin = Pajaro(2,'negro',1000)
piolin.nacer()
piolin.hablar()
piolin.volar(100)