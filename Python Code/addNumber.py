import re

def add(numbers):
    if not numbers:
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[numbers.index("\n")+1:]

    numbers = re.split(f"[{delimiter}\n]", numbers)
    negatives = [int(num) for num in numbers if int(num) < 0]

    if negatives:
        raise Exception("Negatives not allowed: " + ", ".join(str(num) for num in negatives))

    return sum(int(num) for num in numbers if int(num) <= 1000)
