# Python Shift Scheduler

Sistema em Python para gerar automaticamente escalas mensais de trabalho para operadores.

## Regras implementadas

* 4 operadores: Sofia, Daniel, Viviane e Jorge
* Turnos de 11 horas
* Dois tipos de turno:

  * **Abertura:** 09:30 – 21:30
  * **Fecho:** 11:00 – 23:00
* Durante a semana sempre há **no mínimo 2 operadores** (abertura e fecho)
* Fins de semana também possuem **2 operadores**
* Quem **fecha não pode abrir no dia seguinte**
* O sistema tenta **equilibrar as horas mensais entre os operadores**
* A escala gerada é **exportada automaticamente para Excel**

## Tecnologias utilizadas

* Python
* OpenPyXL
* Estrutura modular de projeto

## Estrutura do projeto

EscalaParaEmpresa/

├─ src/
│  ├─ gerador_escala.py
│  ├─ balanceador.py
│  ├─ export_excel.py

├─ main.py
└─ README.md

## Como executar

Clone o repositório:

git clone https://github.com/DanielVianaz/the-python-shift-scheduler.git

Entre na pasta do projeto:

cd the-python-shift-scheduler

Execute o programa:

python main.py

## Saída do programa

O sistema gera automaticamente uma **planilha Excel com a escala mensal dos operadores**, facilitando o planejamento e reduzindo a necessidade de criação manual de escalas.
