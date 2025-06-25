diccionario={'c1':'valor1', 'c2':'valor2'}
cliente={'nombre':'edwin', 'peso':40, 'talla':1.76}
dic={"c1":55,"c2":[10,20,30], "c3":{"s1":23}}
dic2={'c1':['a','b','c'],'c2':['d','e','f']}
dicadd={'v1':'a', 'v2':'b'}
mayuscula=dic2['c2'][1].upper()
# CREAR NUEVA CLAVE
dicadd['v3']='c'
# MODIFICAR O SOBREESCRIBIR
dicadd['v1']='A'
# CONOCER LA LLAVES
print(dicadd.keys())
# CONOCER LOS VALORES
print(dicadd.values())
# CONOCER TODOS OS VALORES
print(dicadd.items())
print(dicadd)
print(mayuscula)
# consulta=cliente['nombre']
# print(dic['c3']["s1"])
# print(consulta)

# print(type(diccionario))
# resultado=diccionario['c1']
# print(resultado)
# print(diccionario)