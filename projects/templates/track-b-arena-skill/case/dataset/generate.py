"""Генератор экземпляров. Один и тот же код и параметры для всех split — меняется только сид.

uv run case/dataset/generate.py --split train --seed 1 --n 20 > train.jsonl
"""
import argparse
import json
import random

SPLIT_SEEDS = {"train": 1000, "public": 2000, "private": 3000}  # private генерируется оператором и не коммитится


def make_instance(rng: random.Random, idx: int) -> dict:
    # TODO: сгенерировать экземпляр задачи и, если нужно, эталон
    return {"id": f"ex-{idx:04d}", "input": {}, "reference": None}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--split", choices=SPLIT_SEEDS, required=True)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--n", type=int, required=True)
    a = p.parse_args()
    rng = random.Random(SPLIT_SEEDS[a.split] + a.seed)
    for i in range(a.n):
        print(json.dumps(make_instance(rng, i), ensure_ascii=False))


if __name__ == "__main__":
    main()
