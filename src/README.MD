# Python Shift Scheduler

Sistema em Python para gerar automaticamente escalas mensais de trabalho.

## Regras implementadas

- 4 operadores: Sofia, Daniel, Viviane e Jorge
- Turnos de 11 horas
- Dois tipos de turno:
  - Abertura: 09:30 – 21:30
  - Fecho: 11:00 – 23:00
- Durante a semana sempre há no mínimo **2 operadores** (abertura e fecho)
- Fins de semana também têm **2 operadores**
- Quem fecha não pode abrir no dia seguinte
- O sistema tenta equilibrar as horas mensais entre os operadores
- A escala gerada é exportada automaticamente para Excel

## Tecnologias

- Python
- OpenPyXL
- Estrutura modular (src)

## Objetivo

Automatizar a geração de escalas mensais para reduzir trabalho manual e facilitar o planejamento operacional.