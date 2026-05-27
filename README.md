# Agent Benchmark: Robustness e Cost

Projeto desenvolvido para o Checkpoint 2 - Sprint 2 da disciplina Tópicos em Engenharia de Software.

## Tema

Avaliação e benchmarks para sistemas agênticos, com foco em:

- Robustness: capacidade do agente manter desempenho diante de entradas ambíguas, incompletas ou com ruído.
- Cost: estimativa de custo operacional por interação, considerando tokens aproximados e tempo de execução.

## Objetivo

O objetivo deste protótipo é simular um agente de atendimento no domínio de varejo e avaliá-lo por meio de cenários controlados.

O sistema executa testes, calcula métricas de sucesso, robustez, número de turnos, tempo médio e custo estimado em tokens.

O protótipo é inspirado na proposta de benchmarks como tau-bench, mas foi implementado de forma simplificada para ser executável localmente, sem dependência de APIs pagas.

## Escopo do Mini-Projeto

O agente simula atendimento para três tipos de solicitação:

1. Consulta de status de pedido.
2. Solicitação de reembolso.
3. Troca de endereço de entrega.

Cada cenário possui uma intenção esperada. O agente tenta identificar a intenção do usuário usando regras simples e retorna uma ação. O avaliador compara a resposta do agente com o comportamento esperado.

## Stack Técnica

- Python 3.10+
- Pytest
- Pandas
- Matplotlib

## Como Rodar

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd agent-benchmark-robustness-cost
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

No Windows Git Bash:

```bash
source venv/Scripts/activate
```

No Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o benchmark

```bash
python -m src.run_benchmark
```

### 5. Rodar os testes

```bash
python -m pytest
```

## Saídas Geradas

Após a execução, o programa gera arquivos na pasta `results/`:

- `benchmark_results.csv`: resultados por cenário.
- `summary_metrics.json`: resumo das métricas.
- `cost_by_scenario.png`: gráfico de custo estimado por cenário.

## Métricas Avaliadas

| Métrica | Descrição |
|---|---|
| Success Rate | Percentual de cenários respondidos corretamente |
| Robustness Score | Desempenho em cenários ambíguos ou com ruído |
| Average Turns | Média de turnos até a resposta |
| Average Latency | Tempo médio de execução |
| Estimated Cost | Custo estimado com base em tokens simulados |

## Integrantes e Responsabilidades

| Integrante | Responsabilidade |
|---|---|
| Elizeu Gonçalves de Oliveira Júnior | Estrutura inicial do projeto e organização do repositório |
| Felipe Viotto Buzziol | Implementação do agente e lógica de classificação |
| Gustavo Miranda dos Santos | Criação dos cenários de avaliação e testes |
| Matheus Mendes Machado | Implementação das métricas e geração dos resultados |
| Vinícius Vedovello Trevisan | Documentação, README e preparação para apresentação |

## Estado Atual do Checkpoint 2

- Código mínimo funcional implementado.
- Projeto instalável e executável localmente.
- README com objetivo, dependências e instruções de execução.
- Métricas iniciais de robustness e cost.
- Estrutura pronta para evolução nos próximos sprints.

## Próximos Passos

- Adicionar mais cenários de teste.
- Comparar duas versões de prompt ou estratégia do agente.
- Refinar a métrica de custo com base em modelos reais.
- Melhorar visualização dos resultados para uso no painel final.
