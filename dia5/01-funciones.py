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
print(checkResul)
# print(resulta)
# resultado=multiplicar(10,20)
# print(resultado)
# print(sumar(2,3))
# print(saludar("edwin"))

