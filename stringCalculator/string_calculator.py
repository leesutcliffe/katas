import re

def add(numbers):

    if numbers == "":
        return 0

    if re.match("\/\/\[(.+)\]", numbers):
        delimiter = re.match("\/\/\[(.+)\]", numbers)[1]
        delimiter = re.escape(delimiter)
        numbers = numbers.strip(f"//[{delimiter}]\n")
    elif numbers[0:2] == "//":
        delimiter = numbers[2]
        numbers = numbers.strip(f"//{delimiter}\n")
    else :
        delimiter = ","

    is_negative = [number for number in re.split(f"{delimiter}|\n", numbers) if int(number) < 0]

    if is_negative:
        raise Exception(f"negatives not allowed: {delimiter.join(is_negative)}")

    numbers = [int(number) for number in re.split(f"{delimiter}|\n", numbers)]

    non_large_numbers = []
    for number in numbers:
        if number < 1001:
            non_large_numbers.append(number)

    return sum(non_large_numbers)
    
    