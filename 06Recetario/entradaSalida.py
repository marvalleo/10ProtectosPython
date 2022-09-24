import os


import os
mi_archivo = open(r'C:\\Users\\Marcelo\Desktop\\ProyectosPython\\06Recetario\\prueba.txt')

print(mi_archivo)
#06Recetario\\\\prueba.txt' mode='r' encoding='cp1252'>
una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea.rstrip())# quita el salto de linea al final 

una_linea = mi_archivo.readline()
print(una_linea)

#o podemos usar un for para recorrer el archivo

for l in mi_archivo:
    print('Aqui dice:',  l)

#o podemos crear una lista con todas las filas

todas = mi_archivo.readlines()
print('todas: ',todas)




mi_archivo.close()