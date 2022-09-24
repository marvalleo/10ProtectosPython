import os
from pathlib import Path

os.system('cls')
#getcwd = get Current Working Directory(directorio de trabajo actual)
ruta = os.getcwd()
print('ruta: ',ruta)

#nombre de base del elemento, nombre de archivo
elemento = os.path.basename(ruta)
print('Elemento1: ', elemento)
#nombre de directorio del elemento
elemento = os.path.dirname(ruta)
print('Elemento2: ', elemento)
#retorn una tupla con la ruta y el nombre del archivo
elemento = os.path.split(ruta)
print('Elemento3: ', elemento)


#chdir Change Directory (cambiar de directorio)
ruta = os.chdir('C:\\Users\\Marcelo\\Desktop\\alternativo')

archivo= open('C:\\Users\\Marcelo\\Desktop\\alternativo\\otro_archivo.txt','r')
print(archivo.read())

archivo.close()

#crea directorio
ruta = os.makedirs('C:\\Users\\Marcelo\\Desktop\\alternativo\\otro')
#eliminad directorio
ruta = os.rmdir('C:\\Users\\Marcelo\\Desktop\\alternativo\\otro')

#para trabajar con un archivo en otro directorio en cualquier OS
#usamos Path

carpeta = Path('C:\\Users\\Marcelo\\Desktop\\alternativo\\otro')
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())







