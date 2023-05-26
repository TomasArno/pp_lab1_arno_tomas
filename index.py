from biblioteca import (
    mostrar_nombre_formateado,
    leer_json,
    mostrar_estadisticas_jugador,
    validador,
    guardar_csv,
    limpiar_consola,
    imprimir_mensaje,
    buscar_mostrar_logros,
)

jugadores = leer_json("./dt.json")


def aplicacion_nba():
    ingresos = []
    while True:
        opcion = input("Elija la opción deseada (0-20): ")
        if validador(r"^[0-9]{1,2}$", opcion) and int(opcion) <= len(jugadores):
            opcion = int(opcion)
            ingresos.append(opcion)
            match opcion:
                case 0:
                    break
                case 1:
                    for jugador in mostrar_nombre_formateado(jugadores):
                        imprimir_mensaje(jugador, "Info")
                    limpiar_consola()
                case 2:
                    estadisticas_jugador = mostrar_estadisticas_jugador(jugadores)
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
                case 4:
                    buscar_mostrar_logros(jugadores)
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    pass
                case 9:
                    pass
                case 10:
                    pass
                case 11:
                    pass
                case 12:
                    pass
                case 13:
                    pass
                case 14:
                    pass
                case 15:
                    pass
                case 16:
                    pass
                case 17:
                    pass
                case 18:
                    pass
                case 19:
                    pass
                case 20:
                    pass
        else:
            imprimir_mensaje("Opción inválida", "Error")


aplicacion_nba()
