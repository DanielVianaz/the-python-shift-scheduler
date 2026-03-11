from src.gerador_escala import gerar_escala
from src.balanceador import rebalancear_horas
from src.export_excel import gerar_excel

ano = 2026
mes = 4

# gerar escala base
escala = gerar_escala(ano, mes)

# rebalancear horas
escala = rebalancear_horas(escala, ano, mes)

# gerar Excel
gerar_excel(escala)