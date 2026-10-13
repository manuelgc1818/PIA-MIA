from datetime import datetime


def limpiar(fila):
    for campo, valor in fila.items():
        if valor is None or valor.strip() == "":
            raise ValueError(f"El campo '{campo}' está vacío")
    #fecha
    try:
        fecha = datetime.strptime(fila["fecha"], "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("La fecha tiene un formato incorrecto")

   #cantidad
    try:
        unidades = int(fila["unidades"])
    except ValueError:
        raise ValueError("Las unidades deben ser un número entero")

   
    if unidades <= 0:
        raise ValueError("Las unidades deben ser mayores que cero")

   #precio
    try:
        precio = float(fila["precio_unitario"].replace(",", "."))
    except ValueError:
        raise ValueError("El precio unitario no es válido")

    # Comprobar que el precio sea positivo
    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero")

    # 5. Devolver la fila limpia
    return {
        "fecha": fecha,
        "producto": fila["producto"].strip(),
        "unidades": unidades,
        "precio_unitario": precio,
        "vendedor": fila["vendedor"].strip()
    }