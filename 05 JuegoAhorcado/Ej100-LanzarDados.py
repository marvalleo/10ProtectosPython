import random

def lanzar_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    

    return dado1,dado2

def evaluar_jugada(a,b):
    suma_dados = a + b

    if suma_dados<= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")

    if 6<suma_dados< 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")

    if 10<=suma_dados:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

a,b = lanzar_dados()
evaluar_jugada(a,b)