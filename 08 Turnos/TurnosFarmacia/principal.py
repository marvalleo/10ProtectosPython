
# Areas:
# -perfumeria P
# -farmacia F
# -cosmetica C
# preguntar area y dar turno
# agregar texto en el turno: Su turno es.... aguarde y será atendido
import keyboard
import numeros


def menu():
    while True:
        
        print('[F] - Farmacia')
        print('[P] - Perfumería')
        print('[C] - Cosmetica')
        print('[S] - para salir del programa.')
        try:
            seleccion = input('Seleccione el numero área deseada: ').upper()
            ['P','F','C','S'].index(seleccion)
        except ValueError:
            print('Esa no es una opcion válida')  
        else:
            if seleccion != 'S':
                numeros.decorador(seleccion)
            else:
                print('Gracias por su visita')
                break

    
    
menu()

