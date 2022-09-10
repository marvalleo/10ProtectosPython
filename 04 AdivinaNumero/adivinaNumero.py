from random import *

nombre = input('Ingresa tu nombre: ')
numeroAzar = randint(1, 101)
intentos = 0
print(f'Ok {nombre} Tienes 8 intentos para adivinar un numero entre 8 y 100.')

while intentos < 8:
    eleccion = int(input('Ingresa un numero: '))
    intentos += 1

    if 100 < eleccion < 0:
        print('El numero está fuera del rango establecido')
    elif eleccion > numeroAzar:
        print('El numero que buscas es menor.')

    elif numeroAzar > eleccion:
        print('El numero que buscas es mayor.')
    else:
        print('FELICITACIONES {nombre}, adivinaste el numero en {intentos} intentos')
        break

print(f'Los siento {nombre} se te acabaron los intentos, el numero era {numeroAzar}.')
