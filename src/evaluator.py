import time
from typing import Dict, List

import pandas as pd

from src.agent import RetailSupportAgent
from src.scenarios import SCENARIOS


def run_evaluation() -> pd.DataFrame:
    agent = RetailSupportAgent()
    rows: List[Dict] = []

    for scenario in SCENARIOS:
        start = time.perf_counter()
        response = agent.answer(scenario["message"])
        latency = time.perf_counter() - start

        success = response.intent == scenario["expected_intent"]

        rows.append(
            {
                "scenario_id": scenario["id"],
                "scenario_type": scenario["type"],
                "message": scenario["message"],
                "expected_intent": scenario["expected_intent"],
                "predicted_intent": response.intent,
                "action": response.action,
                "success": success,
                "turns": response.turns,
                "estimated_tokens": response.estimated_tokens,
                "estimated_cost_usd": estimate_cost(response.estimated_tokens),
                "latency_seconds": latency,
            }
        )

    return pd.DataFrame(rows)


def estimate_cost(tokens: int) -> float:
    return round((tokens / 1000) * 0.00015, 8)


def summarize_results(df: pd.DataFrame) -> Dict:
    ambiguous = df[df["scenario_type"] == "ambiguous"]
    
    success_rate = float(df["success"].mean())

    return {
        "total_scenarios": int(len(df)),
        "success_rate": round(success_rate, 4),
        "success_percentage": round(success_rate * 100, 2),
        "robustness_score": round(float(ambiguous["success"].mean()), 4)
        if len(ambiguous) > 0
        else None,
        "average_turns": round(float(df["turns"].mean()), 4),
        "average_latency_seconds": round(float(df["latency_seconds"].mean()), 6),
        "total_estimated_tokens": int(df["estimated_tokens"].sum()),
        "total_estimated_cost_usd": round(float(df["estimated_cost_usd"].sum()), 8),
    }
