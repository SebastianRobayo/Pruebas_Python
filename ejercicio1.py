# Al quitarle cuatro kilos al peso de al hipopótamo se obtiene dos veces el peso de la jirafa y si sumamos los pesos del hipopótamo y la jirafa se obtiene cinco veces el peso de 
# Elefante(todos en pesos enteros). En la zoológico se dice que un animal es tipo 'uno' si está entre 0 y 20 kilos, tipo 'dos' si está entre 21 y 40 kilos, tipo 'tres si está 
# entre 41 y 80 kilos y tipo 'cuatro' si está por encima de 80 kilos. Dado el peso de la jirafa, realizar un programa que imprima en la primera línea los pesos de la jirafa, 
# el hipopótamo y el elefante separados por un solo espacio y en la segunda línea indique que tipo es el Elefante.

# Entrada:

# Un número entero que representa el peso de la jirafa

#  Salida:

# En la primera línea tres números enteros separados por espacio que representan los pesos de la jirafa, el hipopótamo y elefante separados por un solo espacio. 
# En la segunda línea se debe indicar que tipo es el elefante escrita en letras minúsculas.

# jirafa = 65 => tres
# hipopotamo = 134 => cuatro
# elefante = 39 => dos

jirafa = int(input())
jirafa - 4
hipopotamo = jirafa * 2 + 4
elefante = (hipopotamo + jirafa) / 5

print(jirafa, end=" ")
print(hipopotamo, end=" ")
print(int(elefante))

if(elefante >= 0 and elefante <= 20):
    print("uno")

if(elefante >= 21 and elefante <= 40):
    print("tres")

if(elefante >= 41 and elefante <= 80):
    print("tres")

if(elefante > 80):
    print("cuatro")

