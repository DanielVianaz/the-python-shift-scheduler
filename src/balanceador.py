import calendar
from datetime import date
import holidays


def calcular_meta_horas(ano, mes):

    feriados = holidays.Portugal(years=ano)

    dias_mes = calendar.monthrange(ano, mes)[1]

    dias_uteis = 0

    for dia in range(1, dias_mes + 1):

        data = date(ano, mes, dia)

        if data.weekday() < 5 and data not in feriados:
            dias_uteis += 1

    return dias_uteis * 8


def calcular_horas_operadores(escala):

    horas = {
        "Sofia": 0,
        "Jorge": 0,
        "Viviane": 0,
        "Daniel": 0
    }

    for dia in escala:

        ab = dia.get("abertura")
        fe = dia.get("fecho")
        fx = dia.get("fecho_extra")

        if ab:
            horas[ab] += dia.get("abertura_horas", 11)

        if fe:
            horas[fe] += dia.get("fecho_horas", 11)

        if fx:
            horas[fx] += dia.get("fecho_extra_horas", 11)

    return horas

def rebalancear_horas(escala, ano, mes):

    meta = calcular_meta_horas(ano, mes)

    while True:

        horas = calcular_horas_operadores(escala)

        mudou = False

        abaixo = [op for op, h in horas.items() if h < meta]
        acima = [op for op, h in horas.items() if h > meta]

        # ------------------------------------------------
        # REGRA 1 — REDISTRIBUIR TURNOS
        # ------------------------------------------------

        for op_baixo in abaixo:

            for op_alto in acima:

                for dia in escala:

                    if (
                        dia.get("fecho") == op_alto
                        and dia.get("abertura") != op_baixo
                    ):

                        dia["fecho"] = op_baixo
                        dia["fecho_turno"] = "11:00-23:00"
                        dia["fecho_horas"] = 11

                        mudou = True
                        break

                if mudou:
                    break

            if mudou:
                break

        if mudou:
            continue

        # ------------------------------------------------
        # REGRA 2 — FALTANDO >= 8 HORAS
        # ------------------------------------------------

        for op_baixo in abaixo:

            faltando = meta - horas[op_baixo]

            if faltando >= 8:

                for dia in escala:

                    if (
                        "fecho_extra" not in dia
                        and dia.get("abertura") != op_baixo
                        and dia.get("fecho") != op_baixo
                    ):

                        dia["fecho_extra"] = op_baixo
                        dia["fecho_extra_turno"] = "11:00-23:00"
                        dia["fecho_extra_horas"] = 11

                        mudou = True
                        break

                if mudou:
                    break

        if mudou:
            continue

        # ------------------------------------------------
        # REGRA 3 — AJUSTE FINO
        # ------------------------------------------------

        for operador, total in horas.items():

            diferenca = meta - total

            if diferenca > 0:

                for dia in escala:

                    if dia.get("fecho") == operador:

                        if dia.get("fecho_horas", 11) == 11:

                            dia["fecho_horas"] = 12
                            dia["fecho_turno"] = "10:00-23:00"

                            mudou = True
                            break

                if mudou:
                    break

            elif diferenca < 0:

                for dia in escala:

                    if dia.get("fecho") == operador:

                        h = dia.get("fecho_horas", 11)

                        novo = max(8, h - 1)

                        if novo != h:

                            dia["fecho_horas"] = novo

                            if novo == 10:
                                dia["fecho_turno"] = "12:00-23:00"
                            elif novo == 9:
                                dia["fecho_turno"] = "13:00-23:00"
                            elif novo == 8:
                                dia["fecho_turno"] = "14:00-23:00"

                            mudou = True
                            break

                if mudou:
                    break

        if not mudou:
            break

    return escala