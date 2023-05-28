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
)

jugadores = leer_json("./dt.json")


def aplicacion_nba():
    ingresos = []
    while True:
        opcion = input("Elija la opción deseada (0-20): ")
        if validador(r"^[0-9]{1,2}$", opcion):
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
                        imprimir_mensaje(
                            "Archivo 'data.csv' guardado satisfactoriamente!",
                            "Success",
                        )
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
                        calcula_promedio_puntos_equipo(jugadores), True, "nombre"
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
                        f"El jugador con mas cantidad de puntos totales es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'puntos_totales','estadisticas')[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 8:
                    imprimir_mensaje(
                        f"El jugador con el mayor porcentaje de tiros de campo es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'porcentaje_tiros_de_campo','estadisticas')[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 9:
                    imprimir_mensaje(
                        f"El jugador con la mayor cantidad de asistencias totales es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'asistencias_totales','estadisticas')[0])}",
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
                        f"El jugador con la mayor cantidad de robos totales es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'robos_totales','estadisticas')[0])}",
                        "Info",
                    )
                    limpiar_consola()
                case 14:
                    imprimir_mensaje(
                        f"El jugador con la mayor cantidad de bloqueos totales es: {mostrar_nombre_formateado(ordenar_lista(jugadores,False,'bloqueos_totales','estadisticas')[0])}",
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
                            "estadisticas",
                        )[:-1]
                    ):
                        imprimir_mensaje(
                            f"{jugador_ordenado['nombre']}: promedio puntos por partido -> {jugador_ordenado['estadisticas']['promedio_puntos_por_partido']}",
                            "Info",
                        )

                    limpiar_consola()
                case 17:
                    limpiar_consola()
                case 18:
                    limpiar_consola()
                case 19:
                    limpiar_consola()
                case 20:
                    limpiar_consola()
        else:
            imprimir_mensaje("Opción inválida", "Error")


aplicacion_nba()
