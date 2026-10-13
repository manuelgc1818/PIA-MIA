#Estadisticas de una lista de notas: media, maximo, minimo y cuantas aprobadas, sin usar statistics.
def nota_media(lista):
    notamedia = 0

    for nota in lista:
        notamedia = notamedia + nota

    notamedia = notamedia / len(lista)

    return notamedia


#lista = [6, 7.5, 8, 6.25, 9]

#media = nota_media(lista)

#print("La nota media es:", media)


def moda(lista):
    num_lista_repetido = 0
    moda = 0

    for nota in lista:
        if lista.count(nota) > num_lista_repetido:
            num_lista_repetido = lista.count(nota)
            moda = nota

    return moda


#lista = [6, 7.5, 8, 6.25, 9]

#moda = moda(lista)

#print("La nota moda es:", moda)

def maximo(lista):
    maximo = lista[0]

    for nota in lista:
        if nota > maximo:
            maximo = nota

    return maximo


#lista = [6, 7.5, 8, 6.25, 9]

#maximo = maximo(lista)

#print("La nota maxima es:", maximo)

def minimo(lista):
    minimo = lista[0]

    for nota in lista:
        if nota < minimo:
            minimo = nota

    return minimo


#lista = [6, 7.5, 8, 6.25, 9]

#minimo = minimo(lista)

#print("La nota minima es:", minimo)

def aprobadas(lista):
    aprobadas = 0

    for nota in lista:
        if nota >= 5:
            aprobadas += 1

    return aprobadas


#lista = [6, 7.5, 8, 6.25, 9]

#aprobadas = aprobadas(lista)

#print("El número de aprobados es:", aprobadas)