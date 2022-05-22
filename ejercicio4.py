# Un Bingo virtual genera todas las noches una lista de las letras ganadoras con su respectivo valor.  Por tal motivo, se desea un módulo automático que ayude al cliente a identificar 
# las letras que acertó con la suma total del valor de todas las letras. Por lo tanto, se requiere un programa que dado un diccionario (en formato JSON) imprima el valor total y las 
# letras que acertó separados por espacio.

# {"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62, "f": 35}
# d p h u i e t q

import json 

entradaBingo = input()
entradaApuesta = input()

resultado = json.loads(entradaBingo)
contador = 0
texto = ''

for letra in entradaApuesta:
    if letra in resultado:
        contador += resultado[letra]
        texto += ' ' + letra

print(contador)
print(texto.strip(' '))
            
