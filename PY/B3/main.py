
from carga import cargar_datos
from limpieza import limpiar
from informe import crear_informe
filas = cargar_datos()
rechazos = []
validas = []

for n, fila in enumerate(filas, start=2):
    try:
        limpia = limpiar(fila)
    except (ValueError, KeyError) as e:

        rechazos.append({"linea": n,
                        "motivo": str(e)})

    continue

validas.append(limpia)
crear_informe(validas)