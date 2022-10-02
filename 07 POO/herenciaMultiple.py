class Padre:
    def hablar(self):
        print('habla')

class Madre:
    def reir(self):
        print('jajaja')

    def hablar(self):
        print('que tal')


class Hijo(Madre, Padre):
    pass


class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)