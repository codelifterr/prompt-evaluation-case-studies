from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RubricItem:
    name: str
    weight: float
    score: float
    note: str


@dataclass(frozen=True)
class EvaluationResult:
    total_score: float
    max_score: float
    percentage: float
    issues: tuple[str, ...]


def evaluate(items: list[RubricItem]) -> EvaluationResult:
    if not items:
        raise ValueError("At least one rubric item is required")
    total = sum(item.weight * item.score for item in items)
    max_score = sum(item.weight * 10 for item in items)
    issues = tuple(item.note for item in items if item.score < 7)
    return EvaluationResult(
        total_score=round(total, 2),
        max_score=round(max_score, 2),
        percentage=round((total / max_score) * 100, 2),
        issues=issues,
    )
