import json
from pathlib import Path

import matplotlib.pyplot as plt

from src.evaluator import run_evaluation, summarize_results


def main() -> None:
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    df = run_evaluation()
    summary = summarize_results(df)

    df.to_csv(results_dir / "benchmark_results.csv", index=False)

    with open(results_dir / "summary_metrics.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2, ensure_ascii=False)

    plt.figure()
    plt.bar(df["scenario_id"], df["estimated_cost_usd"])
    plt.title("Custo estimado por cenario")
    plt.xlabel("Cenario")
    plt.ylabel("Custo estimado em USD")
    plt.tight_layout()
    plt.savefig(results_dir / "cost_by_scenario.png")

    print("Benchmark executado com sucesso!")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
