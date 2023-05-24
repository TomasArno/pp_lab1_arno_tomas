import json
import re


def leer_json(nombre_archivo: str) -> list[dict]:
    """
    Esta función lee el archivo JSON indicado por parámetro y devuelve el contenido de la key "jugadores"
    parseado como una lista de diccionarios
    """
    with open(nombre_archivo) as archivo:
        return list[dict](json.load(archivo)["jugadores"])


def validador(patron: str, opcion_evaluar: str):
    if re.match(patron, opcion_evaluar):
        return True
    else:
        return False


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


def mostrar_estadisticas_jugador(jugadores: list[dict]) -> None:
    """
    Esta función le pide al usuario que ingrese el indice de un jugador para luego imprimir todas las estadísticas del mismo formateadas

    :param jugadores: Lista de diccionarios que contiene los datos de todos los jugadores
    return: None
    """
    lista_nombres = mostrar_nombre_formateado(jugadores)
    contador = 0
    for nombre in lista_nombres:
        print(f"#{contador} - {nombre}")
        contador += 1

    indice = input("Ingrese el indice del jugador a buscar: ")
    validado = validador(r"[0-9]{1,2}$", indice)

    if validado and int(indice) <= len(jugadores):
        lista_jugadores = jugadores[:]
        indice = int(indice)
        for key in lista_jugadores[indice]["estadisticas"]:
            print(
                f"{key.lower().capitalize()}: {lista_jugadores[indice]['estadisticas'][key]} \n"
            )

    else:
        print("Dato ingresado inválido")
