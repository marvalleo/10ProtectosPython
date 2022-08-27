texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5] #imprime de la posicion 2 a la 5
print(fragmento)
###############################################
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:]   #imprime desde la posicion 2 hasta el final
print(fragmento)
##################
texto = "ABCDEFGHIJKLM"
fragmento = texto[:5] #imprime desde el principio hasta la posicion 5
print(fragmento)
##################
texto = "ABCDEFGHIJKLM"
fragmento = texto[:] #imprime todo el texto
print(fragmento)
##################
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5:3] #imprime de la posicion 2 a la 5 saltando de 3 en 3
print(fragmento)
#####################################
texto = "ABCDEFGHIJKLM"
fragmento = texto[::-1] #imprime el texto al reves
print(fragmento)
#####################################
texto = "ABCDEFGHIJKLM"
fragmento = texto[::-3] #imprime el texto saltando de 3 en 3 al reves
print(fragmento)

#####################################
frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase[:9]
print(fragmento)





