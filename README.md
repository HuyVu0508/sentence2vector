# Efficient Grammatical and Semantic Sentence Embeddings Framework

## Abstraction
- Proposing a framework for sentence embedding that captures both semantic and grammatical information.
- Designing model to learn 2 tasks: relevant sentence detection (semantic task) and POS tags prediction (grammar task).
- Designed to decrease number of parameters, save computation cost.
- Can be considered unsupervised learning.
- Proposed model is an improvement from the original paper [1] – Quick-Thought model.

## Introduction
- Sentence embedding is the task of representing a sentence as a numeric vector. This representations are usually used for transfer-learning tasks.
- The goal is to have a representation that captures as much information of the sentence as possible.
- Can be done in an unsupervised, or supervised manner.

## Proposed method
We design our model to solve 2 tasks:

### Semantic learning task - Classifying relevant sentences:
Given the input sentence 𝑠 and a set of candidate sentences 𝑆_𝑐𝑎𝑛𝑑. The model has to point out the relevant context sentence 𝑠_𝑐𝑡𝑥𝑡. 

### Grammatical learning task – Predicting POS tags:
The model learns to predict POS tags for each word in the sentence. The loss is the cross entropy between predictions and POS tags labels.

### Computing Total Loss:
Total loss is the weighted sum of losses from two learning tasks. The weight 𝛼 is a hyper-parameter used to regularize semantic and grammartical learning task.

## Experiements
We test our encoder on 4 downstream tasks:
- SICK: Sentence relatedness score prediction
- CR: Movie review sentiment classification
- MSRP: Parapharse identification 
- TREC: Question classification task










