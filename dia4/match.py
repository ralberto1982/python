cliente={   'nombre':'Edwin',
            'edad':'43',
            'ocupacion':'Desarrolador' }

pelicula={   'titulo':'Matrix',
            'Ficha':{'protagonista':'keanu',
                     'director':'lana y lili'},
           }
elementos=[cliente, pelicula, 'libro']

for e in elementos:
       match e:
              case{'nombre':nombre,
                   'edad':edad,
                   'ocupacion':ocupacion}:
                     print('es un cliente')
                     print(nombre,edad,ocupacion)
              case{'titulo':titulo,
                   'ficha':{'protagonista':protagonista,
                            'director':director}
                   }:
                     print('es una pelicula')
                     print(titulo,protagonista,director)
                     
              case _:
                     print('no se que es')

