from os import system

system("cls")

lista=list(range(1,20))
contador=0
listaPares=[]

for num in lista:
    if num % 2 == 0:
        contador=contador + 1
        listaPares.append(num)
    else:
       pass
   
   
print(f" Los numeros pares son: {listaPares} \n Cantidad de numeros pares: {contador}")