# generadores
# decoradores OK

def farmacia():
    for n in range(1, 101):
        yield f'F-{n}'


def perfumeria():
    for n in range(1, 101):
        yield f'P-{n}'


def cosmetica():
    for n in range(1, 101):
        yield f'C-{n}'


f = farmacia()
p = perfumeria()
c = cosmetica()

def decorador(rubro):
    print('\n'+'*'*20)
    print('Su numero es:')
    if rubro == 'P':
        print(next(p))
    elif rubro == 'F':
        print(next(f))
    elif rubro == 'C':
        print(next(c))
    print('Aguarde y será atendido')
    print('\n'+'*'*20)