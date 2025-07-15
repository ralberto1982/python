# las funciones nos permiten crear bloques de codigo que luego 
# sea reutilizado
# codigo mas dinamico este se da cuando utilizamos todo lo referente
# a la programacion ejempo loops, iteradores, conidicionales, metodos etc

def  saludar(nombre=""):
 return (f"hola {nombre}")


def sumar(num1="", num2=""):
   return num1 + num2

def multiplicar(num1="", num2=""):
   return num1 * num2

def chequearcifras(numero):
  return numero in range(100, 1000)

# comprobar una lista
def chequear3cifras(lista):
    lista3=[]
    for n in lista:
       if n in range(100,1000):
         lista3.append(n)
    else:
       pass
    
    return lista3

       
checkResul= chequear3cifras([555, 99, 600])
resulta=chequearcifras(25)
# print(checkResul)
# print(resulta)
# resultado=multiplicar(10,20)
# print(resultado)
# print(sumar(2,3))
# print(saludar("edwin"))


# ejemplo de funcion

preciosCafe=[('Capuchino',2.5),('Expreso',1.2),('moka',1.9)]

# for iten in preciosCafe:
#    print(iten)

def cafeMasCaro(listaPrecio):
   precioMayor=0
   cafeMasCaro=''
   for cafe , precio in listaPrecio:
      if precio > precioMayor:
         precioMayor =precio
         cafeMasCaro= cafe
      else:
         pass

   return (cafeMasCaro,precioMayor)

# print(cafeMasCaro(preciosCafe))

# interacion  entre funciones


# argumentos variables
# *args

# sin args
def suma(a,b):
   suma= a+b
   return suma


# con args
def sum(*args):
   total=0
   # sum(args)
   for arg in args:
      total= total + arg
   return total


# **kwargs para trabjar con diccionarios

def suma(**kwargs):
   totales = 0
   for clave, valor in kwargs.items():
      print(f"{clave } es igual a {valor}")
      totales += valor
   return totales


def sumando(num1,num2,*args,**kwargs):
   print(f"elprimer  valor es {num1}")
   print(f"el segundo valor es {num2}")

   for arg in args:
      print(f"arg = {arg}")

   for clave, valor in kwargs.items():
      print(f"{clave } = {valor}")
      

   return ""


args=[300,400,500]
kwargs={'x':3,'y':5,'z':2}
print(sumando(15,50,args,kwargs))
