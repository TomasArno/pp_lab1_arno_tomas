import json
import re
import os


_b_red: str = "\033[41m"
_b_green: str = "\033[42m"
_b_blue: str = "\033[44m"
_f_white: str = "\033[37m"
_no_color: str = "\033[0m"


def imprimir_mensaje(mensaje: str, tipo_mensaje: str) -> None:
    """
    This function prints a message with a specified type (error, success, or info) in a colored format.
    :param mensaje: a string containing the message to be printed
    :param tipo_mensaje: The parameter "tipo_mensaje" is a string that represents the type of message
    that will be printed. It can be "Error", "Success", or "Info"
    """
    match tipo_mensaje.strip().capitalize():
        case "Error":
            print(f"{_b_red}{_f_white}> Error: {mensaje}{_no_color}")
        case "Success":
            print(f"{_b_green}{_f_white}> {mensaje}{_no_color}")
        case "Info":
            print(f"{_b_blue}{_f_white}> {mensaje}{_no_color}")


def limpiar_consola() -> None:
    """
    This function clears the console screen and waits for user input to continue.
    """
    _ = input("Presione una tecla para continuar...")
    if os.name in ["ce", "nt", "dos"]:
        os.system("cls")
    else:
        os.system("clear")


def validador(patron: str, opcion_evaluar: str) -> bool:
    """
    Esta función se encarga de validar con REgex un determinado patron proveído por el usuario.
    :param patron: Str que contiene el patron a analizar sobre el texto.
    :param opcion_evaluar: Str que contiene el texto a ser analizado.

    return: Bool indicando si pasó o no la validación
    """
    if re.search(patron, opcion_evaluar):
        return True
    else:
        return False


def ordenar_lista(lista, orden: bool) -> list:
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for rango_a in range(len(lista) - 1):
            if (
                orden
                and lista[rango_a] > lista[rango_a + 1]
                or not orden
                and lista[rango_a] < lista[rango_a + 1]
            ):
                lista[rango_a], lista[rango_a + 1] = (
                    lista[rango_a + 1],
                    lista[rango_a],
                )
                flag_swap = True

    return lista


def leer_json(nombre_archivo: str) -> list[dict]:
    """
    Esta función lee el archivo JSON indicado por parámetro y devuelve el contenido de la key "jugadores"
    parseado como una lista de diccionarios
    """
    with open(nombre_archivo) as archivo:
        return list[dict](json.load(archivo)["jugadores"])


def guardar_csv(nombre_archivo: str, data: dict) -> None:
    """
    Esta función guarda en un archivo .CSV la data recibida por parámetro, si el archivo no existe lo creará.

    :param nombre_archivo: String que representa el nombre del archivo a guardar|crear
    :param data: Dict que contiene la información a guardar
    """
    with open(nombre_archivo, "w") as archivo:
        if data:
            data_jugadores = []
            campos = []
            data_jugador = []
            for elemento in data:
                if elemento:
                    if data[elemento] and type(data[elemento]) is dict:
                        for value in data[elemento]:
                            campos.append(str(value))
                            data_jugador.append(str(data[elemento][value]))
                    elif type(data[elemento]) != list:
                        campos.append(str(elemento))
                        data_jugador.append(str(data[elemento]))

            data_jugadores.append(", ".join(campos))
            data_jugadores.append(", ".join(data_jugador))

            archivo.write("\n".join(data_jugadores))
        else:
            imprimir_mensaje("La data a guardar no debe ser vacía", "Error")


def mostrar_nombre_formateado(jugador: dict):
    """
    Esta función imprime el nombre del jugador formateado

    :param jugador: diccionario que contiene los datos de un jugador
    return: None
    """
    if jugador:
        return f'{jugador["nombre"]} - {jugador["posicion"]}'
    else:
        imprimir_mensaje("Elemento vacío", "Error")


def mostrar_estadisticas_jugador(jugadores: list[dict]) -> dict:
    """
    Esta función le pide al usuario que ingrese el indice de un jugador para luego imprimir y retornar todas las estadísticas del mismo

    :param jugadores: Lista de diccionarios que contiene los datos de todos los jugadores
    return: Dict que contiene la data del jugador elegido.
    """

    contador = 0
    for jugador in jugadores:
        imprimir_mensaje(f"#{contador} | {mostrar_nombre_formateado(jugador)}", "Info")
        contador += 1

    indice = input("Ingrese el indice del jugador a buscar: ")
    validado = validador(r"^[0-9]{1,2}$", indice)

    if validado and int(indice) <= len(jugadores):
        indice = int(indice)
        imprimir_mensaje(f"#{contador} | {jugadores[indice]['nombre']}:", "Success")

        for key in jugadores[indice]["estadisticas"]:
            imprimir_mensaje(
                f"{key.lower().capitalize()}: {jugadores[indice]['estadisticas'][key]}",
                "Info",
            )
        return jugadores[indice]
    else:
        imprimir_mensaje("Dato ingresado inválido", "Error")


def buscar_mostrar_logros(jugadores: list[dict]) -> list[dict]:
    """
    Esta función busca todos los logros del jugador indicado.

    :param jugadores: Lista de diccionarios que contiene los datos de todos los jugadores.
    return: lista de diccionarios que contiene los datos del jugador deseado
    """
    bandera_entro = False
    lista_jugadores_buscados = []
    for jugador in jugadores:
        imprimir_mensaje(mostrar_nombre_formateado(jugador), "Info")
    nombre_jugador = input(
        "Ingrese el nombre del jugador que quiere ver sus logros: "
    ).lower()
    for jugador in jugadores:
        if jugador and validador(rf"^{nombre_jugador}", jugador["nombre"].lower()):
            bandera_entro = True
            lista_jugadores_buscados.append(jugador)

    if bandera_entro:
        return lista_jugadores_buscados
    else:
        imprimir_mensaje("Ingrese un nombre valido", "Error")
        return -1


def calcula_promedio_puntos_equipo(jugadores: list[dict]) -> None:
    """
    Esta función calcula y muestra el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.

    :param jugadores: Lista de diccionarios que contiene los datos de todos los jugadores.
    """
    acumulador_puntos = 0
    contador_jugadores = 0
    jugadores_validados = []

    for jugador in jugadores:
        if jugador:
            acumulador_puntos += jugador["estadisticas"]["promedio_puntos_por_partido"]
            contador_jugadores += 1
            jugadores_validados.append(jugador["nombre"])
    jugadores_ordenados = ordenar_lista(jugadores_validados, True)

    imprimir_mensaje(
        f"El promedio de puntos total del equipo es de: {int(acumulador_puntos / contador_jugadores)}",
        "Success",
    )

    for nombre_jugador in jugadores_ordenados:
        imprimir_mensaje(
            f"{nombre_jugador}: promedio puntos por partido -> {jugador['estadisticas']['promedio_puntos_por_partido']}",
            "Info",
        )


def pertenece_salon_fama(jugadores: list[dict]) -> None:
    """
    Esta funcion muestra por consola si el jugador indicado pertenece al salon de la fama o no

    :param jugadores: Lista de diccionarios que contiene los datos de todos los jugadores.
    return: None
    """
    bandera_entro = False
    jugadores_buscados = buscar_mostrar_logros(jugadores)
    if jugadores_buscados != -1:
        for jugador in jugadores_buscados:
            for logro in jugador["logros"]:
                if validador(rf"^miembro", logro.lower()):
                    bandera_entro = True
                    imprimir_mensaje(
                        f"{jugador['nombre']} Pertenece al salon de la fama del baloncesto",
                        "Success",
                    )
        if not bandera_entro:
            imprimir_mensaje(
                "El jugador NO pertenece al salon de la fama del baloncesto", "Error"
            )
