"""Crea un programa que le ayude a calcular las comisiones 
de los vendedores el programa le debe perdir:
el nombre
el valor sobre el que se calcularan las comisiones
nota: las comisiones seran del 13%, redondear a maximo 2 decimales
-no olvidardar dar formato a las respuestas

"""

print("\n CALCULADORA DE COMISIONES \n")

nombre= input("Ingresa tu nombre por favor: ")
valorBase=int(input("Ingresa el valor base para calcular comisiones: "))
resultado=(valorBase * 13) /100

comisiones=round(resultado,2)


# comisiones=((valorBase * 13) / 100) 
print()


print("RESULTADOS OBTENIDOS \n")

print(f"SEÑOR/A:  {nombre}, SUS COMISIONES HAN SIDO CALCULADAS \n")
print(f"EL VALOR BASE PARA CALCULO ES: {valorBase} \n")
print(f"SUS COMISIONES TIENEN UN VALOR DE: {comisiones}, MUCHAS GRACIAS ")
print("\n================================================================\n")



