texto="ABCDEFGHIJKLM"
fragmento=texto[2]
# desde donde hasta donde
fragmento=texto[2:5]
# si dejo 1 numero y los dos puntos me mostrara desde hasta el final
fragmento=texto[2:]
# desde o hasta
fragmento=texto[:5]
# con un tercer parametro le indico a que indices ir saltando
fragmento=texto[1:10:3]
# del 0 al ultimo de tanto en tanto
fragmento=texto[::3]
# al reves
fragmento=texto[::-1]



print(fragmento)