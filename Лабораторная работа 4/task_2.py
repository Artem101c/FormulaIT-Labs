import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Преобразование из CSV в JSON"""
    with open(INPUT_FILENAME, "r") as f:
        reader = csv.DictReader(f)
        array_ = []

        for row in reader:
            array_.append(row)

    with open(OUTPUT_FILENAME, "w") as f:
        text_ = json.dumps(array_, indent=4)
        f.write(text_)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
