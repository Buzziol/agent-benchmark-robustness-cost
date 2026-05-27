# Arquitetura do Protótipo

## Visão Geral

O protótipo possui quatro módulos principais:

1. `agent.py`: implementa o agente de atendimento.
2. `scenarios.py`: define os cenários de avaliação.
3. `evaluator.py`: executa o agente nos cenários e calcula métricas.
4. `run_benchmark.py`: gera arquivos de resultado e gráfico.

## Fluxo

Cenário de teste -> Agente -> Resposta -> Avaliador -> Métricas -> Resultados

## Métricas

- Success Rate
- Robustness Score
- Average Turns
- Average Latency
- Estimated Tokens
- Estimated Cost
