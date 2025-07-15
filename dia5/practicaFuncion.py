from random import *

# Práctica Crear Funciones 1
# Declara una función llamada saludar, que cada vez 
# que sea llamada imprima en pantalla "¡Hola mundo!"
# Solo debes definir la función, no debes invocarla luego.

def saludar():
    print("hola mundo")


# Práctica Crear Funciones 2
# Declara una función llamada bienvenida, que tome como
# argumento el nombre de una persona, y que cada vez que sea
# llamada imprima en pantalla
# "¡Bienvenido {nombre_persona}!"
# Crea la variable nombre_persona, y almacena dentro de 
# la misma el nombre que prefieras.
# Solo debes definir la función y crear la variable, 
# no debes invocar la función luego.

def bienvenida(nombre):
    print(f"hola {nombre}")




# Práctica Crear Funciones 3
# Declara una función llamada cuadrado, que tome como
# argumento un número cualquiera, y que cada vez que sea
# llamada, imprima en pantalla el cuadrado de dicho número
# (es decir, la potencia 2 del valor).
# El nombre del argumento que debe tomar dicha función
# es un_numero. Crea dicha variable y asígnale un número cualquiera.
# Solo debes definir la función y crear la variable, 
# no debes invocar la función luego

def cuadrado(num):
    print(num**num)

# Práctica Return 4
# Crea una función llamada potencia que tome dos valores numéricos 
# como argumentos. Deberá devolver el número que resulte de resolver
# una potencia, utilizando el primer número como base, y el segundo
# como exponente


def potencia(nun1="", nun2=" "):
    operacion=nun1**nun2
    return operacion

resultado=potencia(3,4)


# Práctica Return 2
# Crea una función llamada usd_a_eur que tome como único
# parámetro un valor numérico (un monto en dólares estadounidenses), 
# y devuelva como resultado el monto equivalente en euros. A fines 
# de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.
# Crea una variable llamada dolares y almacena en ella un monto
# cualquiera para entregárselo a tu función y evaluar su resultado.

def conversion(cantidad=""):
    usd=cantidad * 0.90
    return usd

divisa=round(conversion(20))



# Práctica Return 3
# Crea una función llamada invertir_palabra que tome los caracteres
# de una palabra dada como argumento, invierta el orden de sus 
# caracteres y los devuelva de ese modo y en mayúsculas.
# Por ejemplo, si le proporcionamos la palabra "Python",
# deberá devolver: "NOHTYP"
# También, deberás crear una variable llamada palabra,
# que contenga el string que tú prefieras, para sumisitrarle 
# como argumento a la función creada.

def invertirPalabra(texto):
    resul=texto[::-1]
    return resul


invertido=invertirPalabra("todos en la cama")



# Práctica Funciones Dinámicas 
# Crea una función (todos_positivos) que reciba una lista de números
# como parámetro, y devuelva True si todos los valores de una lista son
# positivos, y False si al menos uno de los valores es negativo. Crea una
# lista llamada lista_numeros con valores positivos y negativos.
listaPositivos=[]
def tPositivos(lista):
    for n in lista:
        if n > 0:
            listaPositivos.append(n)
        else:
             listaPositivos.append(n)
    return listaPositivos

checkPositivos=tPositivos([1,3,-5])
# print(checkPositivos)


# Práctica Funciones Dinámicas 
# Crea una función (suma_menores) que sume los números de una lista
# (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 
# y menores a 1000, y devuelva el resultado de dicha suma.

def sumaMenores(lista=""):
    nunm=[]
    lista_n=0
    for n in lista:
        if n > 0 and n < 1000:
            lista_n=lista_n + n

        else:
           nunm.append(n)  
    return lista_n, nunm

sumam=sumaMenores([10,20,200, 2000,1100])
# print(sumam)

# Práctica Funciones Dinámicas 
# Crea una función (cantidad_pares) que cuente la cantidad de números 
# pares que existen en una lista (lista_numeros), y devuelva el resultado
#  de dicha cuenta.

def cantidadPares(listanumerosp):
      cant=0
      for n in listanumerosp:
          if n % 2 == 0:
              cant = cant + 1
          else:
              pass
      return cant

paresResult=cantidadPares([2,1,4,6,8])
# print(paresResult)

# Práctica sobre Interacción entre Funciones 
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
# La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
# Dicha función no debe requerir argumentos para funcionar, sino que debe
# generar internamente los valores aleatorios.
# Proporciona el resultado de estos dos dados a una función que se llame 
# evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos)
# y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
# Si la suma es menor o igual a 6:
# "La suma de tus dados es {suma_dados}. Lamentable"
# Si la suma es mayor a 6 y menor a 10:
# "La suma de tus dados es {suma_dados}. Tienes buenas chances"
# Si la suma es mayor o igual a 10:
# "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
# Pistas: utiliza el método choice o randint de la biblioteca random para
# elegir un valor al azar entre 1 y 6.


def lanzarDado():
    lista=[1,2,3,4,5,6]
    # shuffle(lista)
    dado1=choice(lista)
    dado2=choice(lista)
    return dado1,dado2



dado1, dado2 =lanzarDado()

def evaluarJugada(dado1,dado2):
    suma=dado1 + dado2
    if suma <= 6:
        print(f"Lasuma de tus datos es {suma}, lamentable")
    elif suma > 6 and suma < 10 :
        print(f"La suma de tus dados es {suma}, tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma}, parece una jugada ganadora")
    return







# Práctica sobre Interacción entre Funciones 
# Crea una función llamada reducir_lista() que tome una lista como argumento
def reducirLista(lista):
    listaNumeros=set(lista)
    mayor=max(listaNumeros)
    listaNumeros.remove(mayor)
    sorted(listaNumeros)
    return listaNumeros

resultado=reducirLista([1,2,3,0,1,8,9,4,2,10])
# print(reducirLista([1,2,3,0,1,8,9,4,2]))
    
# (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados 
# (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto.
# El orden de los elementos puede modificarse.
# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
# Crea una función llamada promedio() que pueda recibir como argumento la lista 
# devuelta por la anterior función, y que calcule el promedio de los valores de 
# la misma. Debe devolver el resultado, sin imprimirlo.

def promedio(lista):
    suma=0
    suma=suma/len(lista)
    for num in lista:
        suma=suma + num
    
    return suma

# print(round(promedio(resultado)))




# Práctica sobre Interacción entre Funciones 
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda 
# (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe 
# recibir argumentos para funcionar.
def lanzarMoneda():
    moneda=['Cara','Cruz']
    resultado=choice(moneda)
    return resultado


resultado=lanzarMoneda()
listaNumeros=[1,2,3,5,6]
# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero,
# debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista 
# de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se "
#  "autodestruirá", y eliminarla (devolverla como lista vacía []).
# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" 
# y devolver la lista intacta.
def probarSuerte(resultado,listaNumeros):
    if resultado=='Cara':
        listaNumeros=listaNumeros=[]
        print(f"La lista fue destruida y nos quedo una lista= {listaNumeros}")
    else:
        print(f"La lista fue salvada {listaNumeros}")

    return ""

# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al
# azar de una secuencia.
print(probarSuerte(resultado,listaNumeros))