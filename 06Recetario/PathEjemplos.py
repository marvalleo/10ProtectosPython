from pathlib import Path
import os

os.system('cls')
#os.system('clear') , en otros OS

#construye objetos en el formato de una ruta de carpetas del SO
guia = Path('Concepcion', 'Chiguayante.txt')
print('guia: ',guia)

#Me da la ruta absoluta al direcotio principal del usuario actual
base = Path.home()
print('base: ', base)

# Entonces si unimos y agregamos...
base = Path.home()
guia2 = Path(base, 'America', 'Chile',Path('Concepcion', 'Chiguayante.txt'))
print('guia2: ',guia2)

#ocupa el path dado y solo agrega el archivo al final
guia3= guia2.with_name('Hualpen.txt')
print('guia3: ',guia3)

# Parent llega hasta un nivel "-1" en la ruta entregada
print('Con parent, guia 2: ', guia2.parent )

# Ejemplo con la carpeta Europa
guiaEuropa = Path(Path.home(),'Europa') #es un objeto iterable

#para encontrar los archivos txt en el directorio Europa
for txt in Path(guiaEuropa).glob('*.txt'):
    print('txt: ', txt)

# **/* para encontrar tooodos los archivos txt en el directorio Europa
for txt in Path(guiaEuropa).glob('**/*.txt'):
    print('txt2: ', txt)

#path relativos, enfocarse en una de las carpetas del path

guia = Path('Europa','España','Sagrada _Familia.txt')
en_europa = guia.relative_to(Path('Europa'))
en_espania = guia.relative_to(Path('Europa', 'España'))

print('en_europa: ',en_europa)
print('en_espania: ',en_espania)
