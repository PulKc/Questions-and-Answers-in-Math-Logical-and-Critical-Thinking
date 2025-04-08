import json

with open("QAMLC_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# This prints 10 questions
print(json.dumps(data[40:50], indent=2))
