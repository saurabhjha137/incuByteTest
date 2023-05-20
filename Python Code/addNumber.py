
def add(numbers):
    if not numbers:
        return 0
    
    delimiter = ","
    number = numbers.split(",")

    return sum(int(num) for num in number if int(num) <= 1000)


print(add("1"))
print(add("1,2,3,4"))