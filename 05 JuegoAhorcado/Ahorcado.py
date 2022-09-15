#importar metodo choice que elija palabra al azar
#funciones para :
#pedir letra
#validar letra
#chequear letra
#ver si ganó
#primero funciones despues codigo completo que las use

from curses.ascii import isalpha
from ntpath import join
import random

def palabra_azar():

    listado_palabras = ['perro', 'gato', 'pato', 'caballo', 'vaca']
    palabra_seleccionada = random.choice(listado_palabras)
    return palabra_seleccionada

def mostrar_guiones(palabra):

    guiones=''
    for letra in palabra:
        guiones= guiones+'_'
    return guiones

def validar_letra(letra):
     return isalpha(letra)
    
def letra_palabra(letra, palabra):
    lst = []
    for pos,char in enumerate(palabra):
        if(char == letra):
            lst.append(pos)
    return lst
    
    
def juego_ahorcado():
    vidas=6
    letras_ingresadas = []
    letras_erroneas = []
    print('Adivina el animal')
    palabra = palabra_azar()
    lista_palabra = list(palabra)    
    palabra_guiones = mostrar_guiones(palabra)
    lista_palabra_guiones = list(palabra_guiones)
    print(palabra_guiones)
    while vidas!=0:
        letra = input('Ingrese una letra: ')
        while True!= validar_letra(letra):
            letra = input('Ingrese una letra: ')
            validar_letra(letra)
        
        letras_ingresadas.append(letra)
        existe_letra = letra_palabra(letra, palabra)
        if existe_letra == []:
            vidas-=1
            print(f'Letra equivocada, perdiste una vida, vidas restantes: {vidas}')
            print ("".join(lista_palabra_guiones))
            letras_erroneas.append(letra)
            
        else:
            for item in existe_letra:
                lista_palabra_guiones[item] = letra
                
            print ("".join(lista_palabra_guiones))
            print('Le apuntaste')
        if '_' not in lista_palabra_guiones:
            print('GANASTE!!')
            break

    print('Perdiste!!!')



# prueba = palabra_azar()
# print(prueba)
# print(mostrar_guiones(prueba))
# print(validar_letra(prueba))

juego_ahorcado()


