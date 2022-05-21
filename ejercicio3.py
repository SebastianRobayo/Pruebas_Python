# Experimento social

# Un psicólogo desea saber el tamaño de los grupos de amigos que entran a un concierto de reggaetón. Se detectó que los asistentes entran uniformados y las camisas tienen una letra que identifican a las tribus urbanas a que pertenecen.
# El psicólogo supone que cuando entran grupos con la misma letra consecutiva son amigos y cuando son letras diferentes o no son consecutivas pertenecen a un grupo de amigos diferentes. Por lo tanto, decide contar las letras iguales seguidas para saber el tamaño de los grupos. Por ejemplo:
# E,E,e,E,E,d,E,E,D,c,C. En este caso, los primeros 5 “E” pertenecen a un grupo “D” es de un solo individuo, EE pertenecen a 2 asistentes que vienen juntos, luego sigue D que viene solo y c que corresponde a 2 personas amigas. Se debe imprimir el tamaño de los grupos.

# Entrada
# La entrada consta de una sucesión de caracteres separados por coma que corresponden a las letras en las camisas de las personas que entran al concierto.

# Salida
# La salida consta de dos líneas: la primera es la sucesión de letras sin repeticiones, en mayúscula y separadas por espacio; la segunda es la cantidad de veces que se repitió la letra en la camisa de los asistentes del concierto de manera consecutiva, separado también por espacio.

entrada = str(input(''))

entradaFormateada = entrada.split(',')

entradaUpperCase = list(map(lambda x: x.upper(), entradaFormateada))

listaTemporal = []
contadorDiferentes = 0

for x in range(len(entradaUpperCase)):
    if x > 0:
        if listaTemporal[contadorDiferentes-1][0] == entradaUpperCase[x]:
            listaTemporal[contadorDiferentes -
                          1][1] = listaTemporal[contadorDiferentes-1][1] + 1
        else:
            listaTemporal.append([entradaUpperCase[x], 1])
            contadorDiferentes += 1
    else:
        listaTemporal.append([entradaUpperCase[x], 1])
        contadorDiferentes += 1

listaAmigos = ''
listaCantidadAmigos = ''

for x, y in listaTemporal:
    listaAmigos += ' ' + x
    listaCantidadAmigos += ' ' + str(y)

print(listaAmigos)
print(listaCantidadAmigos)