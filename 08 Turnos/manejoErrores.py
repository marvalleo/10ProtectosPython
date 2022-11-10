import os
os.system('cls')
# def suma():
#     n1 = int(input('ingrese un numero:'))
#     n2 = int(input('ingrese otro numero:'))
#     print(n1+n2)
#     print('Gracias por sumar' + n1)


# try:
#     #codigo a probar
#     suma()
# except TypeError:
#     #codigo a ejecutar si hay un error
#     print('Intentaste concatenar tipos distintos')
# except ValueError:
#     print('Ese no es un numero')
# else:
#     #codigo a ejecutar si no hay un error
#     print('hiciste todo bien')
# finally:
#     #codigo que se va a ejecutar de todos modos
#     print('Eso fue todo')


def pedir_numero():

    while True:
        try:
            numero=int(input("Dame un numero:"))
        except:
            print('Ese no es un numero')
        else:
            print(f'ingresaste el numero {numero}')
            break

    print('Gracias')

pedir_numero()

