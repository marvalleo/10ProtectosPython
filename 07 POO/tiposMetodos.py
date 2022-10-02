class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
    def piar(self):
        print(f'Pio, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pajaro volo {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es de color {self.color}')

    @classmethod #no necesitan una instancia para ejecutarse
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print('El pajaro está mirando.')



piolin = Pajaro('amarillo', 'canario')
piolin.volar(50)
piolin.piar()
piolin.pintar_negro()
piolin.alas=False
print('piolin.alas: ', piolin.alas)
Pajaro.poner_huevos(3)
Pajaro.mirar()