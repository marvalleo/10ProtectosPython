texto = input('Ingrese un texto :')
a = input('Ingrese una letra :')
b = input('Ingrese otra letra :')
c = input('Ingrese oootra letra :')

# teMxto = 'marcelo martinez'

ctaa = texto.lower().count(a.lower())
ctab = texto.lower().count(b.lower())
ctac = texto.lower().count(c.lower())
print(f'La letra {a} aparece {ctaa} veces')
print(f'La letra {b} aparece {ctab} veces')
print(f'La letra {c} aparece {ctac} veces')

listaPalabras = texto.split()
ctaPalabras = len(listaPalabras)
print(f'el texto contiene {ctaPalabras} palabras.')

print('La primera Letra es: ',texto[0])
print('La ultima Letra es: ',texto[-1])

listaPalabras = texto.split()
listaPalabras.reverse()
listaInvertida = ' '.join(listaPalabras)
print(listaInvertida)

busqueda = texto.lower().find('python')
#o
#busqueda = 'python' in texto

if busqueda == -1:
    print('No se encuentra la palabra Python')
else:
    print('Si se encuentra la palabra Python')