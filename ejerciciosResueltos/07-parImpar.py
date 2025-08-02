from os import system

system("cls")

numero=int(input("Ingrese un numero: "))

if numero % 2 ==0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")