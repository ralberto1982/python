# Práctica Control de Flujo 1
# Utilizando las variables num1 y num2, que se alimentan 
# con el input del usuario (tal como en el código ya proporcionado):
# Crea una estructura de control de flujo que compare 
# los valores de las variables, y arroje un resultado de 
# acuerdo al caso:
# "num1 es mayor que num2"
# "num2 es mayor que num1"
# "num1 y num2 son iguales"
# Debes mostrar en pantalla el valor de las variables ingresadas
# en lugar de num1 y num2.
# Aclaración:
# 1. No deben imprimirse strings adicionales a la
# respuesta del usuario.



# num1=input("Por favor ingrese un numero:")
# num2=input("Por favor ingrese otro numero:")

# if num1 > num2:
#     print(f"El numero mayor es el numero: {num1}")
# elif num2 > num1:
#     print(f"El numero mayor es el numero: {num2}")
# else:
#     print(f" Los numeros ingresados son iguales: {num1} = {num2}")




# Práctica Control de Flujo 2
# Las leyes de un país establecen que un adulto puede conducir
# si tiene licencia para hacerlo, y para optar por una licencia
# para conducir, debe de tener 18 años o más.
# Crea una estructura condicional para verificar si una persona
# de 16 años sin licencia puede conducir, y muestra el resultado
# que corresponda en pantalla:
# "Puedes conducir"
# "No puedes conducir aún. Debes tener 18 años y contar con una "
# "licencia"
# "No puedes conducir. Necesitas contar con una licencia"
# Utiliza la base de código ya proporcionada para plantear la 
# estructura de control de flujo apropiada y verificar dichas 
# condiciones.

edad=18
menor="Para conducir debes ser mayor de edad y contar con una licencia"
licencia=False
mayor ="Puedes conducir"

# if edad == 18 and licencia == True:
#     print(mayor)
# elif edad == 18 or licencia ==False:
#     print("Aunque eres mayor debes tener licencia de conduccion")
# else:
#     print(menor)


# Práctica Control de Flujo 3
# Para acceder a un determinado puesto de trabajo, el candidato
# debe ser capaz de programar en Python y tener conocimientos de
# inglés.
# Crea una estructura condicional para evaluar a un candidato 
# dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
idioma="ingles"
lenguaje="python"
mensaje1="Cumples con los requisitos para postularte"
mensaje2= "Para postularte, necesitas saber programar en python y tener conocimientos de ingles"
mensaje3= "Para postularte, necesitas tener conocimientos de ingles"
mensaje4 ="Para postularte, necesitas saber programar en python"
# Utiliza la base de código ya proporcionada para plantear
# la estructura de control de flujo apropiada y verificar dichas condiciones.
#  Evalúa a un candidato que sabe inglés, pero no programa en Python.

if lenguaje=="python" and idioma=="ingles":
    print(mensaje1)
if lenguaje=="otro" and idioma == "ingles":
    print(mensaje4)
if lenguaje =="python" and idioma=="otro" :
    print(mensaje3)
else:
    print(mensaje2)

