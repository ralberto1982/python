# Práctica Zip 1
# Muestra en pantalla frases como la del siguiente ejemplo:
# La capital de Alemania es Berlín
# Utiliza la función zip, loops, y las siguientes listas de 
# países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
union=list(zip(paises,capitales))
# print(union)


# for pais, capital in union:
#     print(f"La capital de {pais} es {capital}")


# Práctica Zip 2
# Crea un objeto zip formado a partir de listas, de un conjunto
# de marcas y productos que tú prefieras, dentro de la variable
# mi_zip.

marcas=["Adidas","Sony","Microsof","Open IA"]
productos=["zapatos","play station","xbox","chapgpt"]

# miZip=list(zip(marcas,productos))
# print(miZip)


# Práctica Zip 3
# Crea el zip con las traducciones los números del 1 al 5 en español,
# portugués e inglés (en el mismo orden), y convierte el objeto
# generado en una lista almacenada en la variable numeros:


# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five

numeros=[1,2,3,4,5]
portugues=["um","dois","tres","quatro","cinco"]
ingles=["one","two","three","four","five"]

traductor=list(zip(numeros,portugues,ingles))
print(traductor)