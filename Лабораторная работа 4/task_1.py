import json

FILE_NAME = "input.json"


def task() -> float:
    """Нахождение произведения суммы из словарей"""
    with open(FILE_NAME) as f:
        file_ = json.load(f)

    composition = [i["score"] * i["weight"] for i in file_]
    return round(sum(composition), 3)


print(task())
