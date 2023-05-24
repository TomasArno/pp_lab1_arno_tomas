import json


def leer_json(nombre_archivo: str) -> list[dict]:
    """
    Esta función lee el archivo JSON indicado por parámetro y devuelve el contenido de la key "jugadores"
    parseado como una lista de diccionarios
    """
    with open(nombre_archivo) as archivo:
        return list[dict](json.load(archivo)["jugadores"])


def mostrar_nombre_formateado(jugadores: list[dict]) -> list[str]:
    """
    Esta función retorna una lista con el nombre de cada jugador junto a su posición

    :param jugadores: Lista de diccionarios que contiene los datos de todos los jugadores
    return: list[str] que representa una lista de nombres formateados
    """
    if jugadores:
        lista_nombres = []
        for jugador in jugadores:
            if jugador:
                lista_nombres.append(f"{jugador['nombre']} - {jugador['posicion']}")
            else:
                print("Elemento vacío")
        return lista_nombres
    else:
        print("Elemento vacío")
