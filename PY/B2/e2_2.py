#Deduplicar conservando el orden de aparición original. Es decir, elimina las copias repetidas de una lista.
def deduplicar(lista):
    deduplicada = []

    for nota in lista:
        if nota not in deduplicada:
            deduplicada.append(nota)

    return deduplicada