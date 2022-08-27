mi_lista = ['a', 'b', 'c']
print(type(mi_lista))
otra_lista = ['hola', 55,6.1]

resultado=len(mi_lista)
print('largo lista:', resultado)

resultado=mi_lista[0]
print(resultado)

resultado=mi_lista[0:2] #funciona similar que con los strings
print(resultado)

uniondelistas = mi_lista+otra_lista
print('union de dos listas: ',uniondelistas)

#a diferencia de los strings, las listas si pueden cambiar el valor de sus elementos
mi_lista[0] = 1
print(mi_lista)

mi_lista.append('d')  #agrega elemento a la lista
print(mi_lista)

mi_lista.pop()  #elimina elemento a la lista, si dejas vacio elimina el ultimo, 
                #sino,  ingresas el numero del indice
print(mi_lista)

eliminado = mi_lista.pop() # con esto puedes almacenar el elemento eliminado
print (eliminado)

print(mi_lista.sort()) #ordena alfabeticamente
print(mi_lista.reverse()) #ordena inversamente





