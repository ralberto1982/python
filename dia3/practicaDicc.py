# Práctica Diccionarios 1
# Crea un diccionario llamado mi_dic que almacene la siguiente información
# de una persona:
# nombre: Karen
# apellido: Jurgens
# edad: 35
# ocupacion: Periodista
# Los nombres de las claves y valores deben ser iguales a la consigna.

diccionario1={

    "nombre":"Edwin",
    "apellido":"Loaiza",
    "edad":35,
    "ocupacion":"desarrollador python"

}

# print(diccionario1)


# Práctica Diccionarios 2
# Crea una función print que devuelva del segundo item de la
# lista llamada points2, dentro del siguiente diccionario.
# Si el valor 300 cambiara en el futuro, el código debería
# funcionar igual para devolver el valor que se encuentre en 
# esa misma posición. Para ello, deberás hacer referencia a los
# nombres de las claves y/o índices según corresponda.

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
# print(mi_dict["puntos"]["points2"][1])


# Práctica Diccionarios 3
# Actualiza la información de nuestro diccionario llamado mi_dic  
# (reasignando nuevos valores a las claves según corresponda), y
# agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
# nombre: Karen
# apellido: Jurgens
# edad: 36
# ocupacion: Editora
# pais: Colombia

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"]=36
mi_dic["ocupacion"]="Editora"
mi_dic["pais"]="colombia"
print(mi_dic)