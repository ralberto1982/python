from random import choice



palabras=["ahorcado","peregrino","luciano","arbol","vaso","televisor","ciudad"]
letrasCorrectas=[]
letrasIncorrectas=[]
intentos= 6
aciertos= 0

juegoTerminado=False

def elegirPalabra(listaPalabras):
    palabraElegida=choice(listaPalabras)
    letrasUnicas=len(set(palabraElegida))
    return palabraElegida, letrasUnicas


def pedirLetra():
    letraElegida=''
    esvalida=False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not esvalida:
        letraElegida=input("Elige una letra: ").lower()
        if letraElegida in abecedario and len(letraElegida) == 1:
            esvalida=True
        else:
            print("No has elegido una lera correcta: ")
    return letraElegida


def mostrarTablero(palabraElegida):
    listaOculta=[]
    for l in palabraElegida:
        if l in letrasCorrectas:
            listaOculta.append(l)
        else:
            listaOculta.append('-')
    print(' '.join(listaOculta))

def chequearLetra(letraElegida,palabraOculta, vidas, coincidencias):
    fin = False
    if letraElegida in palabraOculta and letraElegida not in letrasCorrectas:
        letrasCorrectas.append(letraElegida)
        coincidencias = coincidencias + 1
    elif letraElegida in palabraOculta and letraElegida in letrasCorrectas:
        print('Ya has encontrado esa letras ingresa otra diferente')
    else:
        letrasCorrectas.append(letraElegida)
        vidas = vidas -1
    if vidas ==0:
        fin=perder()
    elif coincidencias == letrasUnicas :
        fin = ganar(palabraOculta)
    return vidas, fin, coincidencias

def perder():
    print("Te has quedado si vidas")
    print("la palabra correcta era:" + palabra)
    return True


def ganar(palabraDescubierta):
    mostrarTablero(palabraDescubierta)
    print("Felicitaciones has encontrado la palabra!!!!")
    return True


palabra, letrasUnicas= elegirPalabra(palabras)
while not juegoTerminado:
    print('\n' + '*' * 20 + '\n' )
    mostrarTablero(palabra)
    print('\n')
    print('Letras incorrectas:  ' + '-'.join(letrasCorrectas)) 
    print(f'vidas: {intentos}')
    print('\n' + '*' * 20 + '\n' )
    letra=pedirLetra()
    intentos,terminado,aciertos=chequearLetra(letra,palabra,intentos,aciertos)
    juegoTerminado=terminado


