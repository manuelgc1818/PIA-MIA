#Carga iris.csv con DictReader, convierte las medidas a float
#y calcula la media por clase.
import csv
from pathlib import Path

RUTA = Path(__file__).parent / "Datos" / "iris.csv"
MEDIDAS = ["largo_pet", "ancho_pet", "largo_sep", "ancho_sep"]

with open(RUTA, newline="") as f:
    filas = list(csv.DictReader(f))


def convertir_tipos():
    for fila in filas:
        for medida in MEDIDAS:
            fila[medida] = float(fila[medida])


def calcular_media():
    convertir_tipos()

    clases = {}

    for fila in filas:
        clase = fila["clase"]

        if clase not in clases:
            clases[clase] = {
                "largo_pet": 0,
                "ancho_pet": 0,
                "largo_sep": 0,
                "ancho_sep": 0,
                "contador": 0
            }

        clases[clase]["largo_pet"] += fila["largo_pet"]
        clases[clase]["ancho_pet"] += fila["ancho_pet"]
        clases[clase]["largo_sep"] += fila["largo_sep"]
        clases[clase]["ancho_sep"] += fila["ancho_sep"]

        clases[clase]["contador"] += 1

    for clase, datos in clases.items():
        contador = datos["contador"]

        print("\nClase:", clase)
        print("Media largo pétalo:", datos["largo_pet"] / contador)
        print("Media ancho pétalo:", datos["ancho_pet"] / contador)
        print("Media largo sépalo:", datos["largo_sep"] / contador)
        print("Media ancho sépalo:", datos["ancho_sep"] / contador)


calcular_media()



