import os
from pathlib import Path, PureWindowsPath

os.system('cls')

#USNDO ESTA LIBRERIA NO HAY QUE ABRIR Y CERRAR EL ARCHIVO

carpeta = Path('c:/Users/Marcelo/Desktop/ProyectosPython/06Recetario/prueba.txt')
#lee archivo
print('Lee el archivo: \n',carpeta.read_text())
#tra el nombre de archivo
print('Trae el nombre archivo: ',carpeta.name)
#trae el sufijo (terminacion) o extencion del archivo
print('Trae la extencion archivo: ',carpeta.suffix)
#trae el nombre sin la extencion
print('trae el nombre sin extencion del archivo: ',carpeta.stem)

if not carpeta.exists():
    print('Existe')
else:
    print('NO Existe')

#trae la ruta de windows con los slash correctos
ruta_windows =PureWindowsPath(carpeta)    
print('Ruta de win: ',ruta_windows)


