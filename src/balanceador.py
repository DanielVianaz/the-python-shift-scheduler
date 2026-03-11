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

    horas = {}

    for dia in escala:

        abertura = dia["abertura"]
        fecho = dia["fecho"]

        horas_abertura = dia.get("abertura_horas", 12)
        horas_fecho = dia.get("fecho_horas", 12)

        horas[abertura] = horas.get(abertura, 0) + horas_abertura
        horas[fecho] = horas.get(fecho, 0) + horas_fecho

    return horas


def rebalancear_horas(escala, ano, mes):

    meta = calcular_meta_horas(ano, mes)

    horas = calcular_horas_operadores(escala)

    for operador, total in horas.items():

        excesso = total - meta

        if excesso <= 0:
            continue

        for dia in escala:

            if excesso <= 0:
                break

            # abertura
            if dia["abertura"] == operador:

                h = dia.get("abertura_horas", 12)

                reducao = min(2, excesso)

                novo_h = h - reducao

                if novo_h < 8:
                    continue

                dia["abertura_horas"] = novo_h

                if novo_h == 11:
                    dia["abertura_turno"] = "09:30-20:30"
                elif novo_h == 10:
                    dia["abertura_turno"] = "09:30-19:30"
                elif novo_h == 9:
                    dia["abertura_turno"] = "09:30-18:30"
                elif novo_h == 8:
                    dia["abertura_turno"] = "09:30-17:30"

                excesso -= reducao

            # fecho
            elif dia["fecho"] == operador:

                h = dia.get("fecho_horas", 12)

                reducao = min(2, excesso)

                novo_h = h - reducao

                if novo_h < 8:
                    continue

                dia["fecho_horas"] = novo_h

                if novo_h == 11:
                    dia["fecho_turno"] = "12:00-23:00"
                elif novo_h == 10:
                    dia["fecho_turno"] = "13:00-23:00"
                elif novo_h == 9:
                    dia["fecho_turno"] = "14:00-23:00"
                elif novo_h == 8:
                    dia["fecho_turno"] = "15:00-23:00"

                excesso -= reducao

    return escala