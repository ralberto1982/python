lista=["a","b","c"]
for letra in lista:
    numero=lista.index(letra) +  1
    print(f" Letra {numero} : {letra}")

lista2=["pablo", "fede", "tuis","juan", "juan"]


for nombre in lista2:
    if nombre.startswith("l"):
        print(nombre)
    else:
       print(nombre)


numero= [1,2,4,5,6]
valor=0


for num in numero:
    valor= valor + num
print(valor)



palabra="python"

for let in palabra:
    print(let)


listaLista=[[1,2], [3,4]]

for a, b in listaLista:
       print(a)
       print(b)



dic={"clave1":"a","clave2":"b","clave3":"c" }

for a,b in dic.items():
    print(a,b)