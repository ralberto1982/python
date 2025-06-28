nombre=['Ana','Hugo','Valeria']
edades=[65,29,42]
ciudad=["Medellin","Bogota","Bello"]
hobby=["futbol","Videojuegos","dance"]

combinados=list(zip(nombre,edades,ciudad,hobby))

for nombre, edad, ciudad, hobby in combinados:
     print(f"{nombre} tiene {edad} años, vive en la ciudad de {ciudad} y le gusta {hobby}")