def tipodefigurita(milista):
    listanueva = []

    for figura in milista:
        if figura not in listanueva:
            listanueva.append(figura)

    return listanueva

def mefaltandeltipodefigurita(listafaltante, listatipo, tipotargeta):
    mefalta = []

    for numero in listafaltante:
        if listatipo[numero] == tipotargeta:
            mefalta.append(numero)

    return mefalta

def notengo(lista1, lista2):
    listafaltante = []

    for elemento in lista1:
        if elemento not in lista2:
            listafaltante.append(elemento)

    return listafaltante

def puedocambiar(targetasotrapersona ,targetasquetinen, targetascambio):
    listatargeta = []

    for targeta in targetascambio:
        if targetasotrapersona[targeta] == targetasquetinen:
            listatargeta.append(targeta)

    return listatargeta