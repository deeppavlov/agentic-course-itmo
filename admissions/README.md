# Допуски к семинарам

Чтобы выступать на семинаре с разбором статьи, сначала нужно сдать **допуск** (см.
[порядок проведения семинара](../seminar.md)). Допуск — это Jupyter-ноутбук с 5 заданиями по
статье. Каждое задание — короткий фрагмент кода на PyTorch, реализующий кусок идеи статьи.

## Как устроены задания

Под заголовком каждого задания указан его тип:

- **что есть что** — названия функций или классов заменены: определите, что чему
  соответствует, и ответьте на вопросы;
- **расхождение со статьёй** — код реализует не то, что описано в статье: найдите это место;
- **перепутаны местами блоки кода** — какой-то блок стоит не на своём месте: найдите его;
- **неверный комментарий** — код корректен, но один комментарий утверждает неправду: найдите
  его;
- **вопрос по коду** — ошибок в коде нет: ответьте на вопросы по статье, опираясь на код.

Для найденного отклонения напишите: где оно, что не так, какое место статьи (раздел /
формула / таблица / цитата) нарушено и как должно быть. Код писать не нужно — достаточно
объяснить словами. Запускать и отлаживать код тоже не нужно: все задания решаются чтением
кода и статьи.

## Как сдать

1. Откройте ноутбук нужной статьи.
2. Ответы пишите в ячейки **«Ваш ответ»** после каждого задания.
3. Отправьте решённый `.ipynb` через форму:
   **<https://forms.yandex.ru/cloud/6ac9778c6214131b297c8a22>**

Допуск выполняется индивидуально (см. правила курса в [README](../README.md)).

## Семинар 1

| Статья | Допуск |
|---|---|
| Mikolov et al., 2013 — [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) | [`sem1/1301.3781-word2vec/admission.ipynb`](sem1/1301.3781-word2vec/admission.ipynb) |
| Sutskever et al., 2014 — [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) | [`sem1/1409.3215-seq2seq/admission.ipynb`](sem1/1409.3215-seq2seq/admission.ipynb) |
| Karpathy et al., 2015 — [Visualizing and Understanding Recurrent Networks](https://arxiv.org/abs/1506.02078) | [`sem1/1506.02078-visualizing-rnns/admission.ipynb`](sem1/1506.02078-visualizing-rnns/admission.ipynb) |

## Семинар 2

| Статья | Допуск |
|---|---|
| Agarwal et al., 2024 — [Many-Shot In-Context Learning](https://arxiv.org/abs/2404.11018) | [`sem2/2404.11018-many-shot-icl/admission.ipynb`](sem2/2404.11018-many-shot-icl/admission.ipynb) |
| Modarressi et al., 2025 — [NoLiMa: Long-Context Evaluation Beyond Literal Matching](https://arxiv.org/abs/2502.05167) | [`sem2/2502.05167-nolima/admission.ipynb`](sem2/2502.05167-nolima/admission.ipynb) |
| Yue et al., 2025 — [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837) | [`sem2/2504.13837-rl-reasoning-boundary/admission.ipynb`](sem2/2504.13837-rl-reasoning-boundary/admission.ipynb) |

## Семинар 3

| Статья | Допуск |
|---|---|
| Laban et al., 2025 — [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120) | [`sem3/2505.06120-lost-in-conversation/admission.ipynb`](sem3/2505.06120-lost-in-conversation/admission.ipynb) |
| Wu et al., 2025 — [CollabLLM: From Passive Responders to Active Collaborators](https://arxiv.org/abs/2502.00640) | [`sem3/2502.00640-collabllm/admission.ipynb`](sem3/2502.00640-collabllm/admission.ipynb) |
| Li et al., 2025 — [In-the-Flow Agentic System Optimization for Effective Planning and Tool Use (AgentFlow)](https://arxiv.org/abs/2510.05592) | [`sem3/2510.05592-agentflow/admission.ipynb`](sem3/2510.05592-agentflow/admission.ipynb) |

## Семинар 4

| Статья | Допуск |
|---|---|
| Chhikara et al., 2025 — [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | [`sem4/2504.19413-mem0/admission.ipynb`](sem4/2504.19413-mem0/admission.ipynb) |
| Wu et al., 2026 — [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493) | [`sem4/2605.12493-longmemeval-v2/admission.ipynb`](sem4/2605.12493-longmemeval-v2/admission.ipynb) |
| Li et al., 2026 — [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/abs/2602.12670) | [`sem4/2602.12670-skillsbench/admission.ipynb`](sem4/2602.12670-skillsbench/admission.ipynb) |

## Семинар 5

| Статья | Допуск |
|---|---|
| Agrawal et al., 2025 — [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457v2) | [`sem5/2507.19457-gepa/admission.ipynb`](sem5/2507.19457-gepa/admission.ipynb) |
| Zhang et al., 2025 — [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954v3) | [`sem5/2505.22954-darwin-godel-machine/admission.ipynb`](sem5/2505.22954-darwin-godel-machine/admission.ipynb) |
| Cemri et al., 2025 — [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657v3) | [`sem5/2503.13657-mast/admission.ipynb`](sem5/2503.13657-mast/admission.ipynb) |

## Семинар 6

| Статья | Допуск |
|---|---|
| Wang et al., 2025 — [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf) | [`sem6/2407.16741-openhands/admission.ipynb`](sem6/2407.16741-openhands/admission.ipynb) |
| Merrill et al., 2026 — [Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868v1) | [`sem6/2601.11868-terminal-bench/admission.ipynb`](sem6/2601.11868-terminal-bench/admission.ipynb) |
| Liu et al., 2025 — [DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks](https://arxiv.org/abs/2504.11358v4) | [`sem6/2504.11358-datasentinel/admission.ipynb`](sem6/2504.11358-datasentinel/admission.ipynb) |
