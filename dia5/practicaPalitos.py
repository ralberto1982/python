from random import shuffle

# lista de los palitos
palitos=['-','--','---','----']
# funcion encargada de mesclar palito
# shuffle(palitos) asi no aria nada shuffle solo no devuelve nada
def mezclar(lista):
    shuffle(lista)
    return lista

# pedir al usuario que elija un  delos cuatro numeros
def probarSuerte():
    intento=''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)


# comprobar el intento del usario
def chequearIntento(lista, intento):
    if lista[intento -1]=='-':
       print('a lavar los platos')
    else:
        print("te has salvado")
        
    print(f"te ha tocado {lista[intento -1]}")



palitosMezclados =mezclar(palitos)
selecion=probarSuerte()
chequearIntento(palitosMezclados,selecion)
