# 📁 QAMLC Dataset Structure

The QAMLC dataset is organized in JSON format. Each entry represents a math, logical, or critical thinking question along with its metadata.

## Dataset Fields

| Field Name        | Description                                                                               | Example                                                        |
|-------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `id`              | Unique numeric identifier for each question                                                | `1`                                                            |
| `question`        | The question text (supports basic text formatting)                                         | `"Identify the next number in this sequence: 2, 4, 6, 8, 10"`  |
| `type`            | Type of question. Possible values: `"open-ended"`, `"true-false"`                          | `"open-ended"`                                                 |
| `answer`          | **String.** Final answer(s) to the question. If there are multiple answers, they are **comma-separated in the order they are asked.**        | `"answer": "6, 12"`                                                                                       |
|                   | For **matching** type: item-count pairs are provided.                                                                                         | `"answer": "🍪🍪🍪🍪: 4, 🍔🍔🍔: 3"`                                                                        |
|                   | For **comparative** or **more/less** type: the selected item group is the answer.                                                            | `"answer": "🍍🍍🍍🍍🍍🍍🍍🍍"`                                                                               |
|                   | For **true-false** questions: a Boolean string.                                                                                               | `"answer": "True"`                                                                                        |
|                   | For **fill-in-the-blanks** with values like tens and ones: responses are comma-separated.                                                    | `"answer": "9, 8"`                                                                                        |
|                   | For **grouping by shape or category**: group-labels are followed by matched items.                                                           | `"answer": "Round shape: 😃😄🌝🍪🏀, Cylindrical: 🔋🛢️"`                                                    |                                                        |
| `solution`        | A list of step-by-step solution explanations                                               | `["Step 1: Add 2", "Step 2: Result = 12"]`                      |
| `difficulty`      | Difficulty level of the question. Possible values: `"Easy"`, `"Medium"`, `"Hard"`           | `"Easy"`                                                       |
| `skills_required` | List of skills required to solve the question                                              | `["Math Reasoning", "Arithmetic"]`                             |

---

## Example Entries

### Example 1:

```json
{
  "id": 3,
  "question": "Can you recognise a pattern in this sequence: 1, 2, 3, 5, 8, 13, 21, 34. Name this pattern and find the next sequence number.",
  "type": "open-ended",
  "answer": "Virahānka numbers or Fibonacci sequence. 55",
  "solution": [
    "We are asked to recognise and name this sequence: 1, 2, 3, 5, 8, 13, 21, 34. Also, we need to find the next sequence number.",
    "Let’s try adding 1 to each item to get the next one.",
    "1",
    "2 + 1 = 3",
    "3 + 1 = 4",
    "5 + 1 = 6",
    "...",
    "They are not following this pattern.",
    "Let’s add them one by one in this sequence: 1, 2, 3, 5, 8, 13, 21, 34.",
    "1 + 2 = 3",
    "2 + 3 = 5",
    "3 + 5 = 8",
    "5 + 8 = 13",
    "13 + 21 = 34",
    "Yes, they are following this pattern. This pattern is called Virahānka numbers or the Fibonacci sequence.",
    "So, the next number would be:",
    "21 + 34 = 55",
    "Therefore, the next Virahānka number or Fibonacci number is 55."
  ],
  "difficulty": "Medium",
  "skills_required": [
    "Math Reasoning"
  ]
},
{
  "id": 44,
  "question": "Group them in tens and ones. 🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢",
  "type": "open-ended",
  "answer": "Tens: 1, Ones: 1",
  "solution": [
    "Let us count them from the left. On reaching a count of 10, we jot them as tens.",
    "Ten: 🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢",
    "Remaining: 🟢",
    "Thus, there are 1 tens and 1 ones."
  ],
  "difficulty": "Easy",
  "skills_required": [
    "Math Reasoning"
  ]
}

---
