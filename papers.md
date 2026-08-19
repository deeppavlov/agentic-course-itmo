- Семинар 1: Модели Трансформеров
    - BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, https://arxiv.org/abs/1810.04805.
        - Сложность 8/10. Статья понятная, но большая.
        - Пререквизиты. Базовое понимание self-attention.
        - Общие слова. С инженерной стороны много примеров решения разных NLP-задач. Много бенчмарков, оценивающих "интеллект" нейросети. Хорошо объяснены концептуальные и архитектурные детали, которые стали классическими (связка pre-train на unsupervised данных и fine-tune на supervised данных, разделение моделей на base и large)
        - Ключевые слова. Masked language modeling, pre-train, fine-tune, downstream tasks, GLUE benchmark, encoder-only transformer.
    - XLNet: Generalized Autoregressive Pretraining for Language Understanding, https://arxiv.org/abs/1906.08237.
        - Сложность 10/10. Для искушённых.
        - Пререквизиты. Глубокое понимание self-attention и BERT. Знание идеи data leakage из датасаинса.
        - Общие слова. Усовершенствованная процедура претрейна для BERT. Чтобы понять query & context streams, нужно сильно напрячь мозг, порисовать картинки и пописать формулы.
        - Ключевые слова. Permuted language modeling, query stream, content stream.
    - (T5) Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer. https://arxiv.org/abs/1910.10683.
        - Сложность 9/10. Нереально большая статья.
        - Пререквизиты. Базовое понимание attention.
        - Общие слова. Исчерпывающее исследование text-to-text tasks. Много инженерных мелочей по типу relative position bias. Много примеров решения NLP-задач.
        - Ключевые слова. Seq2seq transformer,
    
    Другие варианты:
    
    - Attention Is All You Need, https://arxiv.org/abs/1706.03762.
        - Сложность 10/10. Понять, что такое self-attention, очень сложно без дополнительных туториалов, гайдов и лекций.
        - Пререквизиты. Желательно базовое знакомство с RNN, умение перемножать матрицы.
        - Общие слова. Базированная база, очередная демонстрация гибкости нейросетей. Глубоко инженерная статья, в которой описаны архитектурные мелочи и разнообразные DL-трюки. Много математики, много текста, мало экспериментов.
        - Ключевые слова. Attention, self-attention, multi-head attention, seq2seq transformer
    - How multilingual is Multilingual BERT? https://arxiv.org/abs/1906.01502.
        - Сложность: 5/10.
        - Пререквизиты. Базовое понимание BERT.
        - Общие слова. Эксперименты, демонстрирующие способности нейросетей. Примеры решения NLP-задач.
        - Ключевые слова. Multilingual model
    - BioBERT: a pre-trained biomedical language representation model for biomedical text mining, https://arxiv.org/abs/1901.08746. FinBERT: Financial Sentiment Analysis with Pre-trained Language Models, https://arxiv.org/abs/1908.10063. SciBERT: A Pretrained Language Model for Scientific Text, https://arxiv.org/abs/1903.10676. BERTweet: A pre-trained language model for English Tweets, https://arxiv.org/abs/2005.10200.
        - Сложность: 6/10.
        - Пререквезиты. Базовое понимание BERT.
        - Общие слова. Эксперименты, демонстрирующие способности нейросетей. Примеры решения NLP-задач.
        - Ключевые слова. Domain adaptation.
    - RoBERTa: A Robustly Optimized BERT Pretraining Approach, https://arxiv.org/abs/1907.11692
        - Сложность 6/10.
        - Пререквизиты. Понимание BERT.
        - Общие слова. Revisited BERT, анализ процедуры обучения.
        - Ключевые слова. Robust optimization, dynamic masking.
    - ALBERT: A Lite BERT for Self-supervised Learning of Language Representations, https://arxiv.org/abs/1909.11942.
        - Сложность 9/10. Большая статья, много математики и инженерии.
        - Пререквизиты. Понимание BERT.
        - Общие слова. Yet another revisited BERT, анализ процедуры обучения.
        - Ключевые слова. Parameter reduction, parameter sharing, scaling models
    - ERNIE: Enhanced Language Representation with Informative Entities, https://arxiv.org/abs/1905.07129.
        - Сложность 9/10. Много математики и инженерии.
        - Пререквизиты. Понимание BERT.
        - Общие слова. Yet another revisited BERT.
        - Ключевые слова. Knowledge graph, Knowledgeable Encoder, injecting knowledge
    - 
    - MPNet: Masked and Permuted Pre-training for Language Understanding, https://arxiv.org/abs/2004.09297.
        - Сложность 7/10. После XLNet не сложно.
        - Пререквизиты. Понимание XLNet.
        - Общие слова. XLNet, из которого убрали лишнее.
        - Ключевые слова. Masked and permuted language modeling.
    - (GPT-1) Improving Language Understanding by Generative Pre-Training, https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf.
        - Сложность 7/10. Небольшая статья.
        - Пререквезиты. Базовое понимание masked self-attention и задачи causal language modeling.
        - Общие слова. Те же, что и для BERT: много архитектурных решений, которые стали мейнстримом. Примеры решения NLP-задач.
        - Ключевые слова. Causal language modeling, pre-train, fine-tune, downstream tasks, GLUE benchmark, decoder-only transformer
    - BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension, https://arxiv.org/abs/1910.13461
        - Сложность 8/10.
        - Пререквизиты. Понимание BERT.
        - Общие слова. Те же, что и для BERT и GPT-1.
        - Ключевые слова. Seq2seq transformer.
- Семинар 2: Извлечение Слотов (Slot Extraction) и Классификация Интентов (Intent Classification)
    
    SQuAD extractive QA:
    
    - (GOLOMB) Goal-Oriented Multi-Task BERT-Based Dialogue State Tracker,  https://arxiv.org/abs/2002.02450
    - BERT-DST: Scalable End-to-End Dialogue State Tracking with Bidirectional Encoder Representations from Transformer, https://arxiv.org/abs/1907.03040
    
    T5-based:
    
    - Dialogue State Tracking with a Language Model using Schema-Driven Prompting, https://arxiv.org/abs/2109.07506
    - Leveraging Slot Descriptions for Zero-Shot Cross-Domain Dialogue State, https://arxiv.org/abs/2105.04222
    
    LLM:
    
    - (FnCTOD) Large Language Models as Zero-shot Dialogue State Tracker through Function Calling, https://arxiv.org/abs/2402.10466
    - Dialog-Post: Multi-Level Self-Supervised Objectives and Hierarchical Model for Dialogue Post-Training, https://aclanthology.org/2023.acl-long.564/
    - TOD-BERT: Pre-trained Natural Language Understanding for Task-Oriented Dialogue, https://aclanthology.org/2020.emnlp-main.66/
    - (DSE) Learning Dialogue Representations from Consecutive Utterance, https://arxiv.org/abs/2205.13568
    
    Дополнительно:
    
    - PLATO: Pre-trained Dialogue Generation Model with Discrete Latent Variable, https://arxiv.org/abs/1910.07931
    - DialogueCSE: Dialogue-based Contrastive Learning of Sentence Embeddings, https://arxiv.org/abs/2109.12599
    - ConveRT: Efficient and Accurate Conversational Representations from Transformers, https://arxiv.org/abs/1911.03688.
        - Сложность 8/10. Много технических деталей и трюков.
        - Общие слова. Эмбединги, полезные при создании диалоговых систем.
- Семинар 3-4: Модели Поиска (Retrieval)
    
    Статьи, которые мы разобрали:
    
    - (ANCE) Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval, https://arxiv.org/abs/2007.00808.
        - Сложность 7/10.
        - Общие слова. Применяется для обучения SOTA текстовых эмбедингов.
        - Ключевые слова. Hard negative mining for contrastive learning.
    - (BGE) C-Pack: Packaged Resources To Advance General Chinese Embedding, https://arxiv.org/abs/2309.07597.
        - Сложность: 6/10.
        - Пререквизиты. Контрастивное обучения. Идея текстовых эмбедингов.
        - Общие слова. Технический отчёт о том, как обучить SOTA текстовые эмбединги.
    - RetroMAE: Pre-Training Retrieval-oriented Language Models Via Masked Auto-Encoder, https://arxiv.org/abs/2205.12035. Condenser: a Pre-training Architecture for Dense Retrieval, https://arxiv.org/abs/2104.08253.
        - Сложность 8/10.
        - Пререквизиты. Хорошее понимание BERT.
        - Общие слова. Статьи о том, как претрейнить language understanding BERT перед тем, как делать из него текстовый энкодер.
    - (Contriever) Unsupervised Dense Information Retrieval with Contrastive Learning, https://arxiv.org/abs/2112.09118
    - How to Train Your DRAGON: Diverse Augmentation Towards Generalizable Dense Retrieval, https://arxiv.org/abs/2302.07452
    
    Дополнительно:
    
    - Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. https://arxiv.org/abs/1908.10084.
        - Сложность 7/10.
        - Общие слова. Первые в природе текстовые эмбединги. Идея би-кодировщика для обучения эмбедингов.
    - SimCSE: Simple Contrastive Learning of Sentence Embeddings, https://arxiv.org/abs/2104.08821.
        - Сложность 8/10.
        - Общие слова. Контрастивное обучение с аугментациями. Достаточно подробно объяснена идея контрастивного обучения эмбедингов. Что-то среднее между Sentence-BERT и тем, что используют сейчас для обучения текстовых эмбедингов.
    - Dense Passage Retrieval for Open-Domain Question Answering, https://arxiv.org/abs/2004.04906
    - Text Embeddings by Weakly-Supervised Contrastive Pre-training, https://arxiv.org/abs/2212.03533
        - просто классная и полезная модель
    - (LABSE) Language-agnostic BERT Sentence Embedding, https://arxiv.org/abs/2007.01852.
        - Сложность 8/10.
        - Пререквизиты. Понимание BERT.
        - Общие слова. Статья о том, как обучить SOTA мультиязычные текстовые эмбединги и где их применять.
    - (OpenAI CLIP) Learning Transferable Visual Models From Natural Language Supervision https://arxiv.org/abs/2103.00020.
        - Сложность 6/10. Объяснения достаточно прозрачные и подробные.
        - Общие слова. Единое пространство эмбедингов для текста и изображений.
        - Ключевые слова. Multimodality
    - Uni-Retriever: Towards Learning The Unified Embedding Based Retriever in Bing Sponsored Search, https://arxiv.org/abs/2202.06212.

В проработке

- Семинар 5: Языковые Модели (LLMs)
    
    Статьи, которые мы разбирали:
    
    - Llama 2: Open Foundation and Fine-Tuned Chat Models, https://arxiv.org/abs/2307.09288.
    - Mixtral of Experts, https://arxiv.org/abs/2401.04088
        - Изменённый слой трансформера, который теперь имитирует ансамбль экспертов.
    - Repetition Improves Language Model Embeddings, https://arxiv.org/abs/2402.15449
    
    Дополнительно:
    
    Концептуальные статьи:
    
    - (GPT-2) Language Models are Unsupervised Multitask Learners, https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf.
        - Сложность 5/10.
        - Пререквизиты. Базовое понимание masked self-attention и задачи language modeling.
        - Общие слова. Статья о том, что нейросеть может выучить, если учить её долго и на больших данных. Много интересных экспериментов с неожиданными для своего времени результатами. Забавная сказка о единорогах в аппендиксе.
    - (GPT-3) Language Models are Few-Shot Learners, https://arxiv.org/abs/2005.14165.
        - Сложность 8/10. Огромная статья.
        - Пререквизиты. Базовое понимание masked self-attention и задачи language modeling.
        - Общие слова. GPT-2 только еще больше компьюта, данных и неожиданных результатов. Первый в природе полноценный промт-инжиниринг.
    - (InstructGPT) Training language models to follow instructions with human feedback, https://arxiv.org/abs/2203.02155
        - Общие слова. Предшественник ChatGPT.
        - Ключевые слова. Reinforcement learning from human feedback.
    - LLM in a flash: Efficient Large Language Model Inference with Limited Memory, https://arxiv.org/abs/2312.11514
        - Оптимизация с точки зрения hardware.
    
    Позиционные эмбеддинги:
    
    - Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation, https://arxiv.org/abs/2108.12409
    - Dissecting Transformer Length Extrapolation via the Lens of Receptive Field Analysis, https://aclanthology.org/2023.acl-long.756/
    - The Impact of Positional Encoding on Length Generalization in Transformers, https://arxiv.org/abs/2305.19466
    
    Трюки для обучения (это не статьи, а просто темы):
    
    - адаптеры (например LoRA https://arxiv.org/abs/2106.09685)
    - Mixed-precision Quantization
    - Post-training Quantization
    - Quantization-aware Training
    - Sharded Training, Sharded Inference
    
    Просто статьи про модели. Большинство статей описывают данные, инженерные фишки в архитектуре, позволяющие ускорять вычисления. Интересные эксперименты и демонстрация возможностей.
    
    - LLaMA: Open and Efficient Foundation Language Models, https://arxiv.org/abs/2302.13971.
    - PaLM: Scaling Language Modeling with Pathways, https://arxiv.org/abs/2204.02311.
    - (Chinchilla) Training Compute-Optimal Large Language Models, https://arxiv.org/abs/2203.15556.
    - BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, https://arxiv.org/abs/2211.05100
    - Model Card and Evaluations for Claude Models, https://www-cdn.anthropic.com/files/4zrzovbb/website/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226.pdf.
    - The Falcon Series of Open Language Models, https://arxiv.org/abs/2311.16867.
    - LaMDA: Language Models for Dialog Applications, https://arxiv.org/abs/2201.08239.
- Семинар 6: Инженерия Промптов и Проблема Галлюцинаций (Prompt Engineering, Hallucination Problem)
    
    Статьи, которые мы разбирали:
    
    - From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting, https://arxiv.org/abs/2309.04269
    - Self-Consistency Improves Chain of Thought Reasoning in Language Models, https://arxiv.org/abs/2203.11171
    - G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment" https://arxiv.org/abs/2303.16634
    
    Дополнительно:
    
    - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, https://arxiv.org/abs/2201.11903
    - Tree of Thoughts: Deliberate Problem Solving with Large Language Models, https://arxiv.org/abs/2305.10601
    - SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models, https://arxiv.org/abs/2303.08896
    - Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation, https://arxiv.org/abs/2305.15852
    - Chainpoll: A high efficacy method for LLM hallucination detection, https://arxiv.org/abs/2310.18344
- Семинар 7: Retrieval Augmented Generation (RAG)
    
    Статьи которые, мы разбирали:
    
    - RAGAS: Automated Evaluation of Retrieval Augmented Generation, https://arxiv.org/abs/2309.15217
    - RA-DIT: Retrieval-Augmented Dual Instruction Tuning, https://arxiv.org/abs/2310.01352
        - одна из техник для совместного обучения LLM и ретривера
    - (GritLM) Generative Representational Instruction Tuning, https://arxiv.org/abs/2402.09906
    
    Дополнительно:
    
    - Re2G: Retrieve, Rerank, Generate, https://arxiv.org/abs/2207.06300
        - одна из техник для совместного обучения LLM, ретривера и реранкера
    - RECOMP: Improving Retrieval-Augmented LMs with Compression and Selective Augmentation
        - предобработка промта
    - (Iter-RetGen) Enhancing Retrieval-Augmented Large Language Models with Iterative Retrieval-Generation Synergy, https://arxiv.org/abs/2305.15294
    - Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection, https://arxiv.org/abs/2310.11511
    - отдельная тема с обзором инструментов?
        - LangChain
        - LlamaIndex
        - что-то еще?
- Семинар 8: Открытое Доменное Вопросно-Ответное Взаимодействие (Open Domain Question Answering) и Вопросно-Ответное Взаимодействие на Основе Знаний (Knowledge-Based Question Answering)
    - [Linking Surface Facts to Large-Scale Knowledge Graphs https://arxiv.org/abs/2310.14909]
    - [Better Together: Enhancing Generative Knowledge Graph Completion with Language Models and Neighborhood Information https://arxiv.org/abs/2311.01326]
    - [(LLaVA) Visual Instruction Tuning https://arxiv.org/abs/2304.08485]