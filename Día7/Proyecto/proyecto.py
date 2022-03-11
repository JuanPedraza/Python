class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta, balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'El cliente {self.nombre} {self.apellido} \n número de cuenta {self.numero_cuenta}: ${self.balance}'

    def depositar(self, monto_deposito):
        self.balance += monto_deposito

    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print('Retiro exitoso')
        else:
            print('fondos insuficientes')

def crear_cliente():
    nombre_cliente = input('Escriba su nombre: ')
    apellido_cliente = input('Escriba su apellido: ')
    cuenta_cliente = input('Escriba su número de cuenta: ')
    cliente = Cliente(nombre_cliente,apellido_cliente,cuenta_cliente)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elige: Depositar(D), Retirar(R), Salir(S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep)
        elif opcion == "R":
            monto_ret = int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print('Gracias por usar su @Juan_pedraza Bank ')

inicio()