palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)

print(lista)

print("\n-------------------------\n")
# forma ma eficiente de crear una lista
palabra = 'python'
lista = [letra for letra in palabra]

print(lista)

print("\n-------------------------\n")

lista = [n for n in range(0,20,2)]

print(lista)

print("\n-------------------------\n")

lista = [n for n in range(0,20,2) if n*2 > 10]
print(lista)
# Y si tengo que poner ELSE

lista = [n if n*2 > 10 else 'no' for n in range(0,20,2)]
print(lista)
print("\n-------------------------\n")

pies=[10,20,30,40,50]
metros=[n*3.281 for n in pies]
print (metros)



