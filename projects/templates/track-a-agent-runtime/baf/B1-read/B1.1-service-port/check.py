"""Чекер B1.1: answer.txt содержит порт из config/app.yaml.

Запуск: python check.py <путь к итоговой рабочей папке>
Вывод: JSON {"pass": bool, "reason": str}
"""
import json
import sys
from pathlib import Path

EXPECTED = "8137"


def main() -> None:
    workdir = Path(sys.argv[1])
    answer = workdir / "answer.txt"
    if not answer.exists():
        result = {"pass": False, "reason": "answer.txt не создан"}
    else:
        value = answer.read_text(encoding="utf-8").strip()
        ok = value == EXPECTED
        result = {"pass": ok, "reason": "ok" if ok else f"ожидалось {EXPECTED}, получено {value!r}"}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
