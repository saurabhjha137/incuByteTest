import re

def add(numbers):
    if not numbers:
        return 0
    
    delimiter = ","
    
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[numbers.index("\n")+1:]
       
    numbers = re.split(f"[{delimiter}\n]", numbers)
    

    return sum(int(num) for num in numbers if int(num) <= 1000)


print(add("//;\n1;2"))
print(add("1\n2"))