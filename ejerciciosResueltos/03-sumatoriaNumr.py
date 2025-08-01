from os import system


system("cls")

lista=list(range(1,8))
sumaPares=0
listaPares=[]
sumaImpares=0
listaImpares=[]


for num in lista:
    if num % 2 ==0:
        sumaPares=sumaPares + num
        listaPares.append(num)
    else:
        sumaImpares=sumaImpares + num
        listaImpares.append(num)
        
print(f" Los numeros pares son: {listaPares} \n Suma de los pares es: {sumaPares} \n Los numeros Impares son: {listaImpares}\n Suma de los impares es : {sumaImpares}")