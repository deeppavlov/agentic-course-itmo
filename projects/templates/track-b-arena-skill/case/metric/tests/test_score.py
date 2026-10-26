"""Тесты метрики. Обязательно — «жульнические» ответы, которые метрика должна ловить."""
import json
import subprocess
import sys
from pathlib import Path

SCORE = Path(__file__).parents[1] / "score.py"


def run(example: dict, answer: str) -> float:
    out = subprocess.run([sys.executable, str(SCORE)], input=json.dumps({"example": example, "answer": answer}),
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)["score"]


def test_wrong_format_gets_zero():
    assert run({"id": "x", "input": {}}, "not a valid answer") == 0.0


# TODO:
# def test_valid_answer_scores_positive(): ...
# def test_constraint_violation_gets_zero(): ...      # например, пересечение трасс / перекрытие деталей
# def test_memorized_answer_from_train_does_not_help(): ...
# def test_better_answer_scores_higher(): ...
