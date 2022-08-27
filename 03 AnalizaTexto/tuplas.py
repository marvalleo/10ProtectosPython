mi_tuple =(1,2,3,4)
print(type(mi_tuple))

t = (5, 5.5, 'texto',[2,3],(5,'k'))

print(mi_tuple[0])
print(mi_tuple[-2])#cuanta al reves

# mi_tuple[0]=10 Las tuplas no permiten asignaciones
print(mi_tuple)
print(t[4][1])

mi_tuple = list(mi_tuple) # Convierte la tupla en lista

mi_tuple = tuple(mi_tuple) # convierte la lista en tupla

w,x,y,z = mi_tuple # solo se puede hacer  cuando existe la misma cantidad de elementos

print(z,y,x,w)

print(mi_tuple.count(1)) #cuenta las apariciones del 1 en la tupla
print(mi_tuple.index(1)) #indica el indice donde se encuentra el 1







