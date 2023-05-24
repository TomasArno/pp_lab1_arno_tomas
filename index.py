from biblioteca import (
    mostrar_nombre_formateado,
    leer_json,
)
import re


jugadores = leer_json("tp_parcial/dt.json")


def aplicacion_nba():
    while True:
        opcion = input("Eliga la opción deseada (0-20): ")
        if re.match(r"[0-9]{1,2}$", opcion) and int(opcion) <= len(jugadores):
            opcion = int(opcion)
            match opcion:
                case 0:
                    break
                case 1:
                    mostrar_nombre_formateado(jugadores)
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
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
            print("Opción inválida")


aplicacion_nba()
