palabra='python'

lista=[]

for letra in palabra:
    lista.append(letra)
print(lista)

# otra forma
lista=[letra for letra in palabra]
print(lista)

# con numeros
lista = [n/2 for n in range(0,21,2)]
print(lista)
# con if
lista = [n/2 for n in range(0,21,2) ]
print(lista)
# con else
lista = [n for n in range(0,21,2) if  n * 2 > 10 ]
print(lista)
lista = [n if  n * 2 > 10  else 'no' for n in range(0,21,2)]
print(lista)

pies = [10,20,30,40,50]

metros = [n * 3.281 for n in pies]
print(metros)
