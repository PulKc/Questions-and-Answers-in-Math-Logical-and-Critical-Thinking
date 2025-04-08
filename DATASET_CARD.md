---
datasets:
- QAMLC
tags:
- mathematics
- logical reasoning
- critical thinking
- educational
- emojis
- grade 6
- step-by-step solutions
- English (UK)
licenses:
- mit
dataset_info:
  features:
  - name: id
    dtype: int32
  - name: question
    dtype: string
  - name: type
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    sequence: string
  - name: difficulty
    dtype: string
  - name: skills_required
    sequence: string
    num_examples: 944
    download_size: ~ 500 kB
---

# Dataset Card for QAMLC

## Dataset Description

- **Dataset Curators:** Pulkit Sahu (VenusMoon)
- **Languages:** English (UK)
- **License:** MIT License

### Dataset Summary

**QAMLC (Questions and Answers in Mathematics, Logical and Critical Thinking)** is a living, open-source dataset designed to enhance mathematical reasoning, logical thinking, and critical analysis skills. It comprises 944 meticulously crafted questions, each accompanied by step-by-step solutions and verified answers, primarily targeting learners up to the Grade 6 level. The dataset uniquely incorporates emojis to represent shapes, promoting visual reasoning.

### Supported Tasks

- **Mathematical Problem Solving:** Enhances basic arithmetic and algebra skills.
- **Logical Reasoning:** Develops the ability to identify patterns and sequences.
- **Critical Thinking:** Encourages analytical thinking through problem-solving.
- **Visual Reasoning:** Utilises emojis to represent shapes, aiding in the recognition and differentiation of visual patterns.

## Dataset Structure

### Data Instances

Each data instance includes:

```json
{
  "id": 1,
  "question": "Identify the next number in this sequence: 2, 4, 6, 8, 10",
  "type": "open-ended",
  "answer": "12",
  "solution": [
    "Given that:",
    "2, 4, 6, 8, 10",
    "We need to find out the next number in this sequence:",
    "2, 4, 6, 8, 10",
    "Let’s find out some patterns between 1 and 3.",
    "Adding 2 to 2 gives 4",
    "2 + 2 = 4",
    "Now let's add 2 to 4",
    "2 + 4 = 6",
    "Similarly,",
    "2 + 6 = 8",
    "2 + 8 = 10",
    "The number in the given sequence is following a pattern: they are increasing by 2.",
    "So, add 2 to the last item in the sequence to get the next unknown number.",
    "2 + 10 = 12",
    "Thus, the next number in this sequence: 2, 4, 6, 8, 10 is 12."
  ],
  "difficulty": "Easy",
  "skills_required": [
    "Math Reasoning"
  ]
}

