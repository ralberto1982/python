
from random import *

# Crea una función llamada devolver_distintos() que reciba 3integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver elnúmero mayor.Si la suma de
# los 3 numeros es menor a 10, va a devolver elnúmero menor.Si la suma de los 3 números 
# es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio.
def distintos(a,b,c):
     suma=a+b+c
     lista= [a,b,c]
     if suma > 15 :
          return max(lista)
     elif suma < 10:
          return min(lista)
     else:
        lista.sort()
        return lista[1]
    



# Escribe una función (puedes ponerle cualquier nombre quequieras) que reciba cualquier 
# palabra como parámetro, y quedevuelva todas sus letras únicas (sin repetir) pero en
# ordenalfabético.Por ejemplo si al invocar esta función pasamos la palabra"entretenido",
# debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']



def palabra(texto):
     miset=set(texto)
     resultado=list(miset)
     resultado.sort()
     return resultado


# print(palabra("pedroo"))

# hotra forma
def listtext(palabra):
     miset=set()
     for letra in palabra:
          miset.add(letra) 
     miset=list(miset)
     miset.sort()

     return miset

# print(listtext("hola"))


# Escribe una función que requiera una cantidad indefinida deargumentos. 
# Lo que hará esta función es devolver True si enalgún momento se ha ingresado 
# al numero cero repetido dosveces consecutivas.Por ejemplo:(5,6,1,0,0,9,3,5) >>> 
# True(6,0,5,1,0,3,0,1) >>> False

def cero(*args):
     cont=0
     for num in args:
          if args[cont]== 0 and args[cont + 1 ]==0:
              return True
          else:
               cont += 1
                 

     return False

# print(cero(1,2,0,3))

# Escribe una función llamada contar_primos() que requiera un 
# solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números 
# primos existentes en el rango que va desde cero hasta ese 
# número incluido, y va a devolver la cantidad de números 
# primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.


def primos(lista):
     numPrimo=0
     numerosel=[]
     for num in lista:
          if num % 1 ==0  and num % num == 0:
               numPrimo= numPrimo + 1
               numerosel.append(num)
               
          else:
               pass
     return numPrimo, numerosel

print(primos(list(range(3,15))))
# print(list(range(1,100)))


def contarPrimos(num):
     primos=[2]
     iteracion = 3
     if num < 2 :
          return 0
     while iteracion <= num:
          for n in range(3, iteracion,2):
               if iteracion % n == 0:
                    iteracion += 2
                    break
          else:
               primos.append(iteracion)
               iteracion += 2
       
     print(primos)
     return len(primos)

print(contarPrimos(10))
               

          
          