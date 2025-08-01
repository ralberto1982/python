from os import system


system("cls")

a=input("ingrese el primer numero: ")
b=input("ingrese el segundo numero: ")
c=input("ingrese el tercer numero: ")

if a>b and a>c:
    print(f"El numero {a} es el numero mayor")
elif b>a and b>c:
    print(f"El numero {b} es el numero mayor")
else:
    print(f"El numero {c} es el numero mayor")
    
    