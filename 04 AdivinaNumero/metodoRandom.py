#distintas formas de escribirlo
import random
from random import randint
from random import *

aleatorio = randint(1,50)
print('aleatorio',aleatorio)
print("\n-------------------------\n")
#valor aleatorio decimal
aleatorio = uniform(1,50)
aleatorio_corto = round(uniform(1,5),1)
print('uniform',aleatorio)
print('con round',aleatorio_corto)

print("\n-------------------------\n")
#numero aleatorio decimal ente 0 y 1
aleatorio = random()
print('random',aleatorio)

print("\n-------------------------\n")
#numero aleatorio decimal ente 0 y 1
colores =['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print('choice',aleatorio)

print("\n-------------------------\n")
numeros = list(range(5,50,5))
shuffle(numeros)
print('shuffle',numeros)

