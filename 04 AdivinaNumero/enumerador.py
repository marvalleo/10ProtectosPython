lista = ['a','b','c','d']
for item in enumerate(lista):
    print(item)
print("\n-------------- ó ------------\n")  

lista = ['a','b','c','d']
for indice, item in enumerate(lista):
    print(indice, item)

print("\n-------------- ó ------------\n")  

lista = ['a','b','c','d']
for indice, item in enumerate(range(50,55)):
    print(indice, item)

print("\n-------------- ó ------------\n")  

lista = ['a','b','c','d']
mis_tuples= list(enumerate(lista))
print(mis_tuples)
