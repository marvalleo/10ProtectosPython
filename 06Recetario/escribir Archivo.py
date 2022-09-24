# "W" hace que el archivo se reemplace por lo que ha en open
#lo sobre escribe

archivo = open('C:\\Users\\Marcelo\Desktop\\ProyectosPython\\06Recetario\\prueba1.txt', 'w')
archivo.write('Soy el nuevo texto') # no agrega salto de linea
archivo.writelines(['Hola', 'mundo', 'aqui', 'estoy'])
archivo.close()

# otra forma con for
archivo = open('C:\\Users\\Marcelo\Desktop\\ProyectosPython\\06Recetario\\prueba1.txt', 'w')
lista = ['Hola', 'mundo', 'aqui', 'estoy']
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

# reemplazar r o w por a, sobre escribe el archivo original agregando una nuevalinea al final
# se usa en los log
archivo = open('C:\\Users\\Marcelo\Desktop\\ProyectosPython\\06Recetario\\prueba1.txt', 'a')
lista = ['Hola', 'mundo', 'aqui', 'estoy', 'otra', 'vez']
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

