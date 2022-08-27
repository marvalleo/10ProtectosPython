# Se puede declarar
set((1, 2, 3, 4, 5))
# O
{1, 2, 3, 4, 5, 6}

# En los set los elementos son unicos
# loe elementos no tienen indice, no tienen orden interno
# los elementos son inmutables

mi_set = set((1, 2, 3, (1, 2, 3), 5, 1, 3, 4, 4))
print(mi_set)

print(len(mi_set))
print(2 in mi_set)  # busca si está el 2 en el set

s1 = {1, 2, 3}
s2 = {'a', 's', 'd'}
s3=s1.union(s2)
print(s3)

s1.add(4) #no agrega repetidos
print(s1)

s1.remove(3) #elimina elemento
print(s1)

s1.discard(6) #es como eliminar, pero esta linea no generará problema
                #ya que aca si discard no encuentra el elemento, pasa de largo
print(s1)

sorteo=s1.pop() #elimina un elemento al azar
print(sorteo)

s1.clear() #vacía el set
print('el set tiene: ')