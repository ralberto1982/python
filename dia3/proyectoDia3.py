
# ===============ANALIZADOR DE TEXTO================
# pedir al ususario que ingrese un texto
# pedir 3 letras a eleccions del usuario
# regresar cuantas veces aparece la letras que eligio
# regresar cuantas palabras hay en el texto
# regresar cual es la primera y ultima letra
# regresar el texto invertido
# verificar si la ´palabra "python" se encuentra en el texto o no


print("\n BIENVENIDO AL ANALIZADOR DE TEXTO \n")
texto=input("Por favor ingresa el texto que desees: \n")
dic={True:"ESTA ", False:"NO ESTA"}
texto=texto.lower()
primera=texto[0]
ultima=texto[-1]
invertido=texto[::-1]
palabras=texto.split(" ")
palabrascantidad=len(palabras)
esta= "python" in texto
conteo=len(texto)
letras=input(" Por favor ingrese 3 letras al azar: \n")
letras=letras.lower()
letras=list(letras)
l1,l2,l3=letras
cl1=texto.count(l1)
cl2=texto.count(l2)
cl3=texto.count(l3)



print("\n RESULTADOS DEL ANALISIS DE TEXTO \n")
print("==================TU TEXTO ES EL SIGUIENTE ================== \n")
print(texto)
print(f" TU TEXTO TIENE {conteo} LETRAS.")
print(f"TU TEXTO ESTA COMPUESTO POR {palabrascantidad} PALABRAS.")
print(f"LAS LETRAS QUE ELEGISTE AL AZAR SON {letras} \n - LA LETRA {l1} SE REPITE {cl1} VECES \n - LA LETRA {l2} SE REPITE {cl2} VECES \n - LA LETRA {l3} SE REPITE {cl3} VECES \n ")
print(f" LA PRIMERA LETRA DEL TETXO ES {primera}")
print(f" LA ULTIMA LETRA DEL TETXO ES {ultima} \n")
print(f" EL TEXTO INVERTIDO QUEDARIA  {invertido} \n")
print(f" LA PALABRA PYTHON {dic[esta]} EN EL TEXTO\n")

print("==================GRACIAS ================== \n")




