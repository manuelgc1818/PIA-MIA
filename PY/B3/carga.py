
def cargar_datos():
    import csv
    from pathlib import Path

    RUTA = Path(__file__).parent / "Datos" / "ventas_sucio.csv"

    with open(RUTA, newline="") as f:
        filas = list(csv.DictReader(f))

    return filas
