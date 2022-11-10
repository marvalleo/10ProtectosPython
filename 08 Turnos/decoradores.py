import os

os.system('cls')


def decorar_saludo(funcion):
    
    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return otra_funcion


@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

mayusculas('Marcelo')

minusculas_decoradas = decorar_saludo(minusculas)
minusculas_decoradas('Martinez')