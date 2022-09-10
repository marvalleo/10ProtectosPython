from random import shuffle

#Lista inicial
palitos =['-','--','---','----']

#Mezclar palitos
def mezclar(palitos):
    shuffle(palitos)
    return palitos

#Pedir intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input('Elige un número del 1 al 4: ')

    return int(intento)

#comprobar intento
def chequear_intento(palitos,intento):
    if palitos[intento -1] == '-':
        print('A lavar los platos')
    else:
        print('Te salvaste')
    
    print(f'Te ha tocado {palitos[intento-1]}')

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)
