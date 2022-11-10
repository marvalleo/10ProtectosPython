def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x*10)
    return lista


def mi_generador():
    lista = []
    for x in range(1, 5):
        yield x*10


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('++++++++++++  OTRO EJEMPLO  ++++++++++++')


def mi_generador2():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador2()
print(next(g))
print(g)
print(next(g))
print(next(g))
