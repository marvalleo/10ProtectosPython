#*Args es un tupla, args  es una convención
def suma(*args):
    total=0

    for arg in args:
        total += arg    
    return total

print(suma(5,6,4,10,100))

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'