"""Tests del motor. Ejecutar con: pytest"""

from motor import (Regla, adelante, atras, cargar, explicar,
                   por_especificidad, por_orden)

REGLAS = cargar("red.yaml")
INICIALES = {"sin_navegacion", "ping_ip_externa_falla", "ping_gateway_falla",
             "sin_ip", "led_red_encendido"}


def test_cargar():
    assert len(REGLAS) == 9
    assert REGLAS[0] == Regla("R1", ("sin_navegacion", "ping_ip_externa_ok"),
                              "problema_dns")



def test_adelante_ejemplo_guiado():
    hechos, traza, _ = adelante(REGLAS, INICIALES)
    assert [regla for _, regla, _ in traza] == ["R5", "R8", "R9"]
    assert "accion_renovar_ip" in hechos


def test_adelante_no_modifica_los_hechos_iniciales():
    copia = set(INICIALES)
    adelante(REGLAS, INICIALES)
    assert INICIALES == copia


def test_adelante_sin_reglas_aplicables():
    hechos, traza, _ = adelante(REGLAS, {"sin_navegacion"})
    assert traza == [] and hechos == {"sin_navegacion"}


def test_refraccion_evita_bucles():
    ciclo = [Regla("A", ("x",), "y"), Regla("B", ("y",), "x")]
    _, traza, _ = adelante(ciclo, {"x"})
    assert [regla for _, regla, _ in traza] == ["A", "B"]


def test_estrategias():
    r0 = Regla("R0", ("sin_navegacion",), "accion_reiniciar_equipo")
    hechos = {"sin_navegacion", "ping_ip_externa_ok"}
    _, t1, _ = adelante([r0] + REGLAS, hechos, por_orden)
    _, t2, _ = adelante([r0] + REGLAS, hechos, por_especificidad)
    assert [r for _, r, _ in t1] == ["R0", "R1", "R2"]
    assert [r for _, r, _ in t2] == ["R1", "R0", "R2"]


def test_explicar_como():
    _, _, origen = adelante(REGLAS, INICIALES)
    lineas = explicar("accion_renovar_ip", origen)
    assert lineas[0] == "accion_renovar_ip: por R9"
    assert "      sin_ip: dato inicial" in lineas


def test_atras_ejercicio_3():
    hechos = {"ping_gateway_falla", "sin_ip", "led_red_apagado"}
    assert atras("accion_revisar_cable", REGLAS, hechos, lambda h, p: False)
    assert "problema_cable" in hechos


def test_atras_pregunta_premisa_primitiva():
    preguntas = []

    def preguntar(hecho, pila):
        preguntas.append((hecho, pila))
        return True

    assert atras("problema_dns", REGLAS, {"sin_navegacion"}, preguntar)
    assert preguntas == [("ping_ip_externa_ok", ("R1",))]


def test_atras_respuesta_negativa():
    assert not atras("problema_dns", REGLAS, {"sin_navegacion"},
                     lambda h, p: False)
