# Las escuelas militares han construido un simulador en la que los futuros soldados entrenan para el combate, los cadetes se le asignan aleatoriamente a uno de dos equipos y estos deben combatir a todos los del otro equipo hasta que se termina el tiempo asignado. 
# Considere dos equipos: comando Furioso y comando Valiente. Solamente un jugador de determinado equipo se enfrenta contra cualquier otro jugador del equipo contrario. Sin embargo, todas las armas están desalineadas, y lo único que se puede hacer es disparar hacia arriba esperando contar con suerte para infligir daño sobre el rival. 
# Cada tipo de arma se va a representar con uno de los siguientes caracteres simétricos: 

#   .
#   -
#   +
#   *
#   T
#   Y
#   |
#   W
#   X
#   M

# Cada comando escoge sus posibles armas con las que se atacará al equipo rival. El reloj de la simulación despliega el arma que sí va a tener efecto contra el otro en cada momento de la simulación. Si algún arma usada por los comandos atina exactamente con la que representa el reloj de la simulación, se anota un punto a dicho equipo y se debe informar el progreso de la puntuación. Para representar el estado del combate en cada momento se usa la siguiente convención: si el comando de los Valientes va ganando, se va a mostrar un 'V', si van empatados un '≈' (ASCII 247 en UTF-8), y si va ganando el comando de los furiosos, se muestra un 'F'. 
# Desarrolle un programa que permita recibir las letras que representan las armas elegidas por cada comando, que reciba la información de las vulnerabilidades a las armas dadas por el reloj de la simulación, y que imprima en pantalla el estado de la simulación en cada momento del tiempo. 


Furioso = input("")
Valiente = input("")
reloj = input("")

resultado = ''
puntaje1 = 1
puntaje2 = 1

for p in reloj:
    if p in Valiente:
        puntaje1 += 1
    if p in Furioso:
        puntaje2 += 1
    if puntaje1 == puntaje2:
        resultado += '≈'
    if puntaje1>puntaje2:
        resultado += 'F'
    if puntaje2>puntaje1:
        resultado += 'V'

print(resultado)
