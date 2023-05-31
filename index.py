from biblioteca import (
    mostrar_nombre_formateado,
    leer_json,
    mostrar_estadisticas_jugador,
    validador,
    guardar_csv,
    limpiar_consola,
    imprimir_mensaje,
    buscar_mostrar_logros,
    calcula_promedio_puntos_equipo,
    pertenece_salon_fama,
    ordenar_lista,
    calcular_max_segun_valor,
    bonus,jugadores_cantidad_posicion
)

jugadores = leer_json("./dt.json")


def aplicacion_nba():
    ingresos = []
    while True:
        opcion = input("Elija la opción deseada (0-22): ")
        if validador(r"^[0-9]{1,2}$", opcion) and int(opcion) <= 22:
            opcion = int(opcion)
            ingresos.append(opcion)
            match opcion:
                case 0:
                    break
                case 1:
                    for jugador in jugadores:
                        imprimir_mensaje(mostrar_nombre_formateado(jugador), "Info")
                    limpiar_consola()
                case 2:
                    estadisticas_jugador = mostrar_estadisticas_jugador(jugadores)
                    limpiar_consola()
                case 3:
                    if 2 in ingresos:
                        guardar_csv("data.csv", estadisticas_jugador)
                    else:
                        imprimir_mensaje(
                            "Por favor, primero solicite las estadisticas de algún jugador",
                            "Error",
                        )
                    limpiar_consola()
                case 4:
                    jugador_buscado = buscar_mostrar_logros(jugadores)
                    if jugador_buscado != -1:
                        for jugador in jugador_buscado:
                            imprimir_mensaje(f"{jugador['nombre']}", "Success")
                            for logro in jugador["logros"]:
                                imprimir_mensaje(logro, "Info")
                    limpiar_consola()
                case 5:
                    for jugador_ordenado in ordenar_lista(
                        calcula_promedio_puntos_equipo(jugadores), True, "nombre", ""
                    ):
                        imprimir_mensaje(
                            f"{jugador_ordenado['nombre']}: promedio puntos por partido -> {jugador_ordenado['estadisticas']['promedio_puntos_por_partido']}",
                            "Info",
                        )
                    limpiar_consola()
                case 6:
                    pertenece_salon_fama(jugadores)
                    limpiar_consola()
                case 7:
                    imprimir_mensaje(
                        f"El jugador con mas cantidad de puntos totales es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'puntos_totales',{})[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 8:
                    imprimir_mensaje(
                        f"El jugador con el mayor porcentaje de tiros de campo es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'porcentaje_tiros_de_campo',{})[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 9:
                    imprimir_mensaje(
                        f"El jugador con la mayor cantidad de asistencias totales es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'asistencias_totales',{})[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 10:
                    calcular_max_segun_valor(jugadores, "promedio_puntos_por_partido")
                    limpiar_consola()
                case 11:
                    calcular_max_segun_valor(jugadores, "promedio_rebotes_por_partido")
                    limpiar_consola()
                case 12:
                    calcular_max_segun_valor(
                        jugadores, "promedio_asistencias_por_partido"
                    )
                    limpiar_consola()
                case 13:
                    imprimir_mensaje(
                        f"El jugador con la mayor cantidad de robos totales es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'robos_totales',{})[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 14:
                    imprimir_mensaje(
                        f"El jugador con la mayor cantidad de bloqueos totales es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'bloqueos_totales',{})[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 15:
                    calcular_max_segun_valor(jugadores, "porcentaje_tiros_libres")
                    limpiar_consola()
                case 16:
                    for jugador_ordenado in calcula_promedio_puntos_equipo(
                        ordenar_lista(
                            jugadores,
                            False,
                            "promedio_puntos_por_partido",
                            {},
                        )[:-1]
                    ):
                        imprimir_mensaje(
                            f"{mostrar_nombre_formateado(jugador_ordenado)}: promedio puntos por partido -> {jugador_ordenado['estadisticas']['promedio_puntos_por_partido']}",
                            "Info",
                        )

                    limpiar_consola()
                case 17:
                    imprimir_mensaje(
                        f"El jugador con la mayor cantidad de logros obtenidos es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'logros',[])[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 18:
                    calcular_max_segun_valor(jugadores, "porcentaje_tiros_triples")
                    limpiar_consola()
                case 19:
                    imprimir_mensaje(
                        f"El jugador con la mayor cantidad de temporadas jugadas es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'temporadas',{})[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 20:
                    calcular_max_segun_valor(
                        ordenar_lista(jugadores, True, "posicion", ""),
                        "porcentaje_tiros_de_campo",
                    )
                    limpiar_consola()
                case 21:
                    bonus(jugadores)
                    limpiar_consola()
                case 22:
                    jugadores_cantidad_posicion(jugadores)
        else:
            imprimir_mensaje("Opción inválida", "Error")


aplicacion_nba()
