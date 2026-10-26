"""Метрика кейса. Формат как в cases/template арены:
stdin — JSON {"example": {...}, "answer": "..."}, stdout — JSON {"score": float}.

Невалидный ответ (формат, нарушение ограничений) получает 0 или штраф — правила фиксируются до поиска.
"""
import json
import sys


def validate(example: dict, answer: str) -> bool:
    # TODO: проверить формат и все жёсткие ограничения задачи
    return False


def quality(example: dict, answer: str) -> float:
    # TODO: посчитать качество валидного ответа
    return 0.0


def main() -> None:
    payload = json.load(sys.stdin)
    example, answer = payload["example"], payload["answer"]
    score = quality(example, answer) if validate(example, answer) else 0.0
    print(json.dumps({"score": score}))


if __name__ == "__main__":
    main()
