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

sumam=sumaMenores([10,20])
