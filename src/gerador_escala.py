import calendar


def gerar_escala(ano, mes):

    operadores = ["Daniel", "Viviane", "Jorge", "Sofia"]

    dias = calendar.monthrange(ano, mes)[1]

    escala = []

    for i in range(dias):

        abertura = operadores[i % 4]
        fecho = operadores[(i - 1) % 4]

        escala.append({
            "dia": i + 1,
            "abertura": abertura,
            "fecho": fecho
        })

    return escala