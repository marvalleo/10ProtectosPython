# Ejercicio 1
def devolver_distintos(x, y, z):

    lista = [x, y, z]
    lista.sort()

    if (x+y+z) > 15:
        return lista[2]
    elif (x+y+z) < 10:
        return lista[0]
    else:
        return lista[1]


print(devolver_distintos(1, 5, 9))

# Ejercicio 2


def ordenar_palabra(word):
    resultado = list(set(word))
    resultado.sort()
    return resultado


print(ordenar_palabra('geeks'))

# Ejercicio 3


def verificar_ceros(*args):
    pivot = 0
    for item in args:
        if item == 0 and pivot == 1:
            return True
        elif item == 0 and pivot == 0:
            pivot = 1
        elif item != 0 and pivot == 1:
            pivot = 0

    return False


print(verificar_ceros(6, 0, 5, 1, 0, 3, 0, 1))

# Ejercicio 4


def contar_primos(numero):

    primos = [2]
    iteracion = 3

    if numero< 2:
        return 0
    
    while iteracion<= numero:

        for n in range(3,iteracion,2):

            pivot= iteracion % n
            if iteracion % n == 0:
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion +=2

    print(primos)
    return len(primos)

print(contar_primos(50))



