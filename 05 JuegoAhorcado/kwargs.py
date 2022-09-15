def suma(**kwargs):
    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total

print(suma(x=3, y=5, z=2))

#####################################################3

def prueba(num1, num2, *args, **kwargs):
    
    print(f'El primer valor es {num1}')
    print(f'El primer valor es {num2}')

    for arg in args:
        print(f'Arg = {arg}')

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
      

prueba(15,50, 100, 200, 300, 400, x='uno', y='dos',z='tres')

#ó
args = [100,200,300,400]
kwargs ={'x':'uno','y':'dos','z':'tres'}
prueba(15,50, *args, **kwargs)

#Crea una función llamada cantidad_atributos que cuente la 
# cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad

#Crea una función llamada lista_atributos que devuelva en forma de lista 
# los valores de los atributos entregados en forma de palabras clave (keywords). 
# La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

#Práctica sobre Argumentos Indefinidos (*kwargs) 3

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')