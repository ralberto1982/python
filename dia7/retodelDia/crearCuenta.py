# crear una clase Persona
# atributos nombre y paellido
# Crear clase Cliente
# atributos numero de cuenta y balance
# metodos imprimir
        # depositar
        # retirar
# codigo
# funciones para crear cliente
# funcion para iniciar e programa puede ser un loop 
# que le pregunte al usuario constante mente que desea hacer
from os import system

class Persona():
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        
class Cliente(Persona):
    def __init__(self, nombre, apellido,numeroCuenta,balance=0):
        super().__init__(nombre, apellido)
        self.numeroCuenta=numeroCuenta
        self.balance=balance
        
    def __str__(self):
        return (f" Cliente:{self.nombre}\n Apellido:{self.apellido}\n Numero de Cuenta: {self.numeroCuenta}\n Balance {self.balance}  ")
    
    
    def depositar(self,montoDeposito):
        self.balance+= montoDeposito
        print("Deposito Aceptado")
    
    
    def retirar(self,montoRetiro):
        if self.balance >= montoRetiro:
           self.balance-= montoRetiro
           print("Retiro Realizado")
        else:
            print("Fondos insuficientes")
  
  
        
    
def crear_Cliente():
        nombreCl=input("Ingrese su Nombre: ")
        apellidoCl=input("Ingrese su Apellido: ")
        numer_cuenta=input("ingrese Numero de cuenta: ")
        cliente=Cliente(nombreCl,apellidoCl,numer_cuenta)
        return cliente



def inicio():
   mi_cliente=crear_Cliente()
   print(mi_cliente)
   opcion=0
   
   while opcion != 'S':
       print('Elige : Depositar (D), Retirar (R), O Salir (S)')
       opcion=input()
       
       if opcion == 'D':
           monto_dep = int(input("Monto a depositar"))
           mi_cliente.depositar(monto_dep)
       elif opcion =='R':
           monto_ret=int(input("Monto a retirar"))
           mi_cliente.retirar(monto_ret)
       print(mi_cliente)
        
print('Gracias por visitarnos y utilizar nuestros sevicios')    
system('cls')
inicio()   