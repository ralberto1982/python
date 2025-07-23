from pathlib import Path

# directorio del ssuario
base=Path.home()

# construir rutas con el objeto path
guia=Path(base, 'barcelona','familia')

# .home() me permite acceder a  una ruta absoluta
guiar=Path(Path.home(),'europa')

# ejemplo ruta base
gia3=Path("europa","españa")

guia2=guia.with_name("lapedraza")

# parent me devuelve la ruta padre de la ruta
# print(guia.parent.parent.parent)

# recuperar porciones de rutas largas nos devuelve un nuevo objeto path
espana=gia3.relative_to(Path("europa","españa"))
europa=gia3.relative_to(Path("europa"))
print(europa)
print(espana)

# recorrer rutas para mostrar elementos
for txt in Path(guiar).glob("**/*.txt"):
    print(txt)







# print(guia2)
