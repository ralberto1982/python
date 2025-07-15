# Práctica sobre Argumentos Indefinidos (*args) 
# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de
# argumentos numéricos, y que retorne la suma de sus valores al cuadrado.
# Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
def sumaCuadrados(*args):
    suma=0
    for num in args:
        resultado =num ** 2
        suma=suma + resultado

    return suma


# print(sumaCuadrados(1,2,3,5))


# Práctica sobre Argumentos Indefinidos (*args) 
# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos
# de cualquier extensión, y retorne la suma de sus valores absolutos (es decir,
#  que tome los valores sin signo y los sume, o lo que es lo mismo, los considere 
#  a todos -negativos y positivos- como positivos).

def sumaAbsolutos(*args):
    suma=0
    for num in args:
        conver=abs(num)
        suma=suma + conver
    return suma

# print(sumaAbsolutos(1,-6,8,-4))

# Práctica sobre Argumentos Indefinidos (*args) 
# Crea una función llamada numeros_persona que reciba,
# como primer argumento, un nombre, y a continuación,
# una cantidad indefinida de números.
# La función debe devolver el siguiente mensaje:
# "{nombre}, la suma de tus números es {suma_numeros}"

def numerosPersona(nombre,*args):

      suma=0
      for num in args:
          suma= suma + num
      return (f'{nombre}, la suma de tus numeros es {suma}')


# print(numerosPersona('edwin',1,2,3))


# Práctica sobre Argumentos Indefinidos (**kwargs) 
# Crea una función llamada cantidad_atributos que cuente
# la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
def cantidad(**kwargs):
    total=0
    for cant in kwargs.items():
        total= total + 1
    return total



# print(cantidad(a=1,b=2,c=3))

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de 
# lista los valores de los atributos entregados en forma de palabras
# clave (keywords). La función debe preveer recibir cualquier cantidad
# de argumentos de este tipo.
def atributos(**kwargs):
    lista=[]
    for atri in kwargs.items():
        lista.append(atri)
    return lista

# print(atributos(a=1,b=2,c=3))

# Práctica sobre Argumentos Indefinidos (**kwargs) 
# Crea una función llamada describir_persona, que tome como parámetros su nombre y
# luego una cantidad indetermida de argumentos.
# Esta función deberá mostrar en pantalla:
# Características |de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:
# describir_persona=("María", color_ojos="azules", color_pelo="rubio")
# Mostrará en pantalla:
# Características de María:
# color_ojos: azules
# color_pelo: rubio

def persona(nombre,**kwargs):
    print(nombre)
    for person,value in kwargs.items():
        print(f" {person} = {value}")
    return ""


print(persona("María", color_ojos="azules", color_pelo="rubio"))