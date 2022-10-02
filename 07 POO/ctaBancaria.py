import os


class Persona():

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido} \n Balance: {self.balance}'

    def depositar(self, monto):
        # cuanto dinero agrega a la cta
        #ingreso = input('Cuanto desea depositar?: ')
        self.balance += int(monto)
        print('Deposito realizado.')

    def retirar(self,egreso):
        # cuanto dinero retirar
        #egreso = int(input('Cuanto desea retirar?: '))

        if egreso > self.balance:
            print('No tiene suficientes fondos')
        else:
            self.balance -= egreso
            print('Retiro realizado.')


# llevar balance    OK
# no retirar mas de lo que se debe     OK
# funcion para crear cliente           ok
# funcion inicio donde el usuario navegue
# codigo para elegir depositar retirar o info cta o salir

def crear_cliente():

    nombre = input('ingrese su nombre: ')
    apellido = input('ingrese su apellido: ')
    ncta = input('ingrese su Numero de cuenta: ')
    #balance = input('ingrese con cuanto dinero iniciará : ')    
    cliente = Cliente(nombre, apellido, ncta)
    return cliente

def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('Presione V para volver al menu: ')

def inicio():

    os.system('cls')
    
    opcion = 0
    while opcion not in range(1,4):
        print('Bienvenido a su cuenta bancaria')
        print(cliente)
        print('''
            Qué desea hacer?

            [1] Deposito
            [2] Retiro
            [3] Salir\n
            ''')
        opcion = int(input('Ingrese su opción: '))
    return opcion

os.system('cls')
opcion = 0
cliente = crear_cliente()
print(cliente)


while opcion != 's':

    menu = int(inicio())
    if menu == 1:
        monto = int(input('ingrese monto a depositar: '))
        cliente.depositar(monto)
        volver_inicio()
        
    elif menu == 2:
        balance = int(input('ingrese con cuanto dinero retirará : '))
        cliente.retirar(balance)
        volver_inicio()
    
    elif menu == 3:
        print('Ha salido del programa.')
        quit()

    print(cliente)
        
        
print('Ha salido del programa.')
quit()

inicio()