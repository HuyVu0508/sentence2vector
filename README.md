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
Given the input sentence and a set of candidate sentences. The model has to point out the relevant context sentence to the input sentence from the set of candidates. This task helps the model learn to capture the semantic information of the input sentence. This idea directly comes from [1]. The loss of this task is the cross entropy loss of the prediction and ground-truth context sentence.

### Grammatical learning task – Predicting POS tags:
The model learns to predict POS tags for each word in the sentence. This task helps the model learn to understand the syntax structure of the input sentence. The loss is the cross entropy between predictions and POS tags labels of all words in the input sentence.

### Computing Total Loss:
The total loss is the weighted sum of losses from two learning tasks. The weight 𝛼 is a hyper-parameter used to regularize semantic and grammartical learning task.

The image below illustrates overview of our model: 
![Optional Text](../master/src/model_overview.png)

## Experiements
We test our encoder on 4 downstream tasks:
- SICK: Sentence relatedness score prediction
- CR: Movie review sentiment  classification
- MSRP: Parapharse identification 
- TREC: Question classification task

## Results and Discussion
- Our model performs as good as the original one on 2 tasks SICK and CR. On MSRP and TREC tasks, our model performs 2-3% better. 
- This increase in accuracy maybe thanks to the ability of our encoder can capture both semantic and grammatical information of a sentence. 
- *Caveat: This performance is not  as high as the model in original paper [1] due to our limited of resources. We test both the original model and our proposed model on a smaller dataset with a shorter training time.*

## Future Works
- Testing on downstream grammatical tasks (object number prediction, word order analysis, top constituents prediction).
- Analyzing effects of regularizor 𝛼 (weights of grammar and semantic learning task) on trained encoder’s quality.
- Simplifying decoder to stress more responsibility on encoder to encode more useful information.

## References
[1]. Lajanugen Logeswaran, Honglak Lee, “An efficient framework for learning sentence representations”. In ICLR, 2018











