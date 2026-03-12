from src.gerador_escala import gerar_escala
from src.balanceador import rebalancear_horas
from src.export_excel import gerar_excel

print("MAIN RODANDO")
def main():

    ano = 2026
    mes = 4

    escala = gerar_escala(ano, mes)

    escala = rebalancear_horas(escala, ano, mes)

    gerar_excel(escala)


if __name__ == "__main__":
    main()