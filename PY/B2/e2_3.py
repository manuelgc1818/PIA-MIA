# Agenda: diccionario de contactos con alta, baja, búsqueda y listado ordenado, en un bucle de menú.
def alta(lista, nombre, telefono):
    if not existe(lista, nombre): 
        lista[nombre] = telefono
    return lista

def baja(lista, nombre):
    if existe(lista, nombre):
        del lista[nombre]
    return lista

def existe(lista, nombre):
    if nombre in lista:
        print("El contacto existe.")
    else:
        print("El contacto no existe.")
    return nombre in lista

def busqueda(lista, nombre):
    if existe(lista, nombre):
        print("El teléfono de", nombre, "es:", lista[nombre])
    else:
        print("No existe.")
lista = {}
opcion=0
while opcion != "4":
    opcion=input("Seleccione una opción: 1. Alta, 2. Baja, 3. Búsqueda, 4.Salir: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        alta(lista, nombre, telefono)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        baja(lista, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        busqueda(lista, nombre)
    elif opcion == "4":
        print("Saliendo del programa.")
