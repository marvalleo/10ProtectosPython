texto = "Este es el texto de Marcelo"
resultado = texto.upper()
print(resultado)
################################################
texto = "Este es el texto de Marcelo"
resultado = texto[2].upper
print(resultado)
################################################
texto = "Este es el texto de Marcelo"
resultado = texto.lower()
print(resultado)
################################################
texto = "Este es el texto de Marcelo"
resultado = texto.split() #separa el texto por espacios generando una lista
print(resultado)
################################################
texto = "Este es el texto de Marcelo"
resultado = texto.split("t") #separa el texto por la letra t generando una lista
print(resultado)
################## JOIN ##############################
a = "Aprender"
b = "Python"
c = "es"
d = "facil"
e = " ".join([a,b,c,d]) #junta los elementos de la lista con un espacio
print(e)
################################################
texto = "Este es el texto de Marcelo"
resultado = texto.find("s") #busca la letra s y devuelve la posicion, si no la encuentra devuelve -1
print(resultado)
################################################
texto = "Este es el texto de Marcelo"
resultado = texto.replace("M","m") #reemplaza la letra M por la letra m
print(resultado)
################################################




