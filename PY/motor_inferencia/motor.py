import json
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Base de conocimiento
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Regla:
    """SI premisas (todas) ENTONCES conclusión."""
    id: str
    premisas: tuple[str, ...]
    conclusion: str


def cargar(ruta):
    """Lee las reglas de un archivo .yaml/.yml o .json.

    Formato: {"reglas": [{"id": ..., "si": [...], "entonces": ...}, ...]}
    """
    with open(ruta, encoding="utf-8") as f:
        if ruta.endswith((".yaml", ".yml")):
            import yaml                      # pip install pyyaml
            datos = yaml.safe_load(f)
        else:
            datos = json.load(f)
    return [Regla(r["id"], tuple(r["si"]), r["entonces"])
            for r in datos["reglas"]]


# ---------------------------------------------------------------------------
# Estrategias de resolución de conflictos
# Reciben el conjunto conflicto (lista de reglas) y devuelven UNA regla.
# ---------------------------------------------------------------------------

def por_orden(conflicto):
    """La primera regla de la lista."""
    return conflicto[0]


def por_especificidad(conflicto):
    """La regla con más premisas (la más concreta). Empate: la primera."""
    return max(conflicto, key=lambda r: len(r.premisas))


# ---------------------------------------------------------------------------
# Encadenamiento hacia delante (guiado por los datos)
# ---------------------------------------------------------------------------

def adelante(reglas, hechos, estrategia=por_orden):
    """Dispara reglas hasta que el conjunto conflicto queda vacío.

    Devuelve:
      hechos  -> set con los hechos iniciales y los deducidos
      traza   -> lista de (ids del conjunto conflicto, regla disparada, hecho nuevo)
      origen  -> diccionario {hecho deducido: regla que lo produjo}
    """
    hechos = set(hechos)              # copia: no modificamos los del usuario
    disparadas, traza, origen = set(), [], {}
    while True:
        # 1. Equiparación: reglas cuyas premisas están todas en la base,
        #    sin contar las ya disparadas (refracción).
        conflicto = [r for r in reglas
                     if set(r.premisas) <= hechos
                     and r.id not in disparadas]
        if not conflicto:
            return hechos, traza, origen
        # 2. Resolución de conflictos
        r = estrategia(conflicto)
        # 3. Ejecución
        disparadas.add(r.id)
        traza.append(([c.id for c in conflicto], r.id, r.conclusion))
        if r.conclusion not in hechos:
            hechos.add(r.conclusion)
            origen[r.conclusion] = r


# ---------------------------------------------------------------------------
# Módulo de explicación: «¿cómo has llegado a esto?»
# ---------------------------------------------------------------------------

def explicar(hecho, origen, nivel=0):
    """Devuelve una lista de líneas con el árbol que justifica un hecho.

    - Si el hecho no está en origen: "hecho: dato inicial".
    - Si está: "hecho: por Rx" y, debajo, la explicación de cada premisa
      de Rx con dos espacios más de sangría por nivel.
    """
    sangria = "  " * nivel
    if hecho not in origen:
        return [f"{sangria}{hecho}: dato inicial"]
    regla = origen[hecho]
    lineas = [f"{sangria}{hecho}: por {regla.id}"]
    for premisa in regla.premisas:
        lineas.extend(explicar(premisa, origen, nivel + 1))
    return lineas


# ---------------------------------------------------------------------------
# Encadenamiento hacia atrás (guiado por los objetivos)
# ---------------------------------------------------------------------------

def atras(objetivo, reglas, hechos, preguntar, pila=()):
    """¿Se puede demostrar objetivo? Añade a hechos lo que demuestra.

    si objetivo está en hechos -> True
    candidatas <- reglas que concluyen objetivo
    si no hay candidatas (premisa primitiva):
        preguntar(objetivo, pila); si responde sí -> añadir a hechos, True
        si no -> False
    para cada regla r en candidatas:
        si TODAS sus premisas se demuestran con
        atras(premisa, reglas, hechos, preguntar, pila + (r.id,)):
            añadir objetivo a hechos, True
    False

    """
    def demostrar(meta, ruta, pila_reglas):
        if meta in hechos:
            return True
        if meta in ruta:
            return False
        candidatas = [r for r in reglas if r.conclusion == meta]
        if not candidatas:
            if preguntar(meta, pila_reglas):
                hechos.add(meta)
                return True
            return False
        for regla in candidatas:
            if all(demostrar(p, ruta + (meta,), pila_reglas + (regla.id,))
                   for p in regla.premisas):
                hechos.add(meta)
                return True
        return False

    return demostrar(objetivo, (), pila)


# ---------------------------------------------------------------------------
# Interfaz de usuario
# ---------------------------------------------------------------------------

def preguntar_consola(hecho, pila):
    """Pregunta «¿Es cierto «hecho»? (s/n/porque)».

    - "porque": muestra "Lo necesito para aplicar " y las reglas de la pila,
      de la más cercana a la más lejana, y vuelve a preguntar.
    - Devuelve True solo si la respuesta es "s".
    """
    while True:
        respuesta = input(f"¿Es cierto '{hecho}'? (s/n/porque): ").strip().lower()
        if respuesta == "porque":
            if pila:
                print("Lo necesito para aplicar " + " -> ".join(reversed(pila)))
            else:
                print("Lo necesito para comprobar el objetivo.")
        elif respuesta in ("s", "n"):
            return respuesta == "s"
        else:
            print("Respuesta no válida. Escribe s, n o porque.")

if __name__ == "__main__":
    reglas = cargar("red.yaml")
    hechos = {"sin_navegacion", "ping_ip_externa_falla"}
    if atras("problema_dns", reglas, hechos, preguntar_consola):
        print("Demostrado: problema_dns")
    else:
        print("No se puede demostrar problema_dns")