#Practica 1
mi_archivo = open('mi_archivo.txt','w')
mi_archivo.write('Nuevo texto')
mi_archivo.close()
mi_archivo = open('mi_archivo.txt','r')
archivo = mi_archivo.readlines()
print(''.join(archivo))
mi_archivo.close()

#Practica 2
mi_archivo = open('mi_archivo.txt','a')
mi_archivo.write("Nuevo inicio de sesión")
mi_archivo.close()
mi_archivo = open('mi_archivo.txt','r')
print(mi_archivo.read())
mi_archivo.close()

#Practica 3
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open('registro.txt', 'a')
for p in registro_ultima_sesion:
    archivo.writelines(p + '\t')
archivo.close()

archivo = open('registro.txt', 'r')
print(archivo.read())
archivo.close()
