from operator import truediv


def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
        

resultado = chequear_3_cifras([444,5,888])
print(resultado)

####################################################
#PRACTICA 1
lista_numeros = [1,2,3]

def todos_positivos(lista_numeros):
    
    for item in lista_numeros:
        if item < 0:
            return False
        else:
            pass
    return True

####################################################
#PRACTICA 2
lista_numeros = [1,2,3]

def suma_menores(lista_numeros):
    suma=0
    
    for item in lista_numeros:
        if item > 0 and item < 1000:
            suma = suma + item
        else:
            pass
    return suma

####################################################
#PRACTICA 3
lista_numeros = [1,2,3]

def cantidad_pares(lista_numeros):
    cuenta=0
    
    for item in lista_numeros:
        if (item%2)==0:
            cuenta += 1
        else:
            pass
    return cuenta






