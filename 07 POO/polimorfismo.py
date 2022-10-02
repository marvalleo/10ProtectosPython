class Vaca:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")



class Oveja:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca1 = Vaca('Aurora')
oveja1 = Oveja('nube')

vaca1.hablar()
oveja1.hablar()

# Ó
print('\n -------- ó -------\n')
animales = [vaca1,oveja1]

for animal in animales:
    animal.hablar()

print('\n -------- ó con funcion -------\n')

def animal_hablar(animal):
    animal.hablar()


animal_hablar(oveja1)