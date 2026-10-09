numbers = [4, 8, 15, 16, 23, 47]

def minimum(numbers:list[int])->int:
    
    minim = float('inf')

    for number in numbers:
        if number < minim:  # noqa: PLR1730
            minim = number
    return int(minim)
def maximum(numbers:list[int])->int:

    maxim = float('-inf')

    for number in numbers:
        if number > maxim: # noqa: PLR1730
            maxim = number
    return int(maxim)

def summation(numbers:list[int])->int:

    sum = 0
    
    for number in numbers:
        sum += number
    return(sum)

def mean(numbers:list[int])->float:

    count = 0
    sum = 0
    for number in numbers:
        count += 1  # noqa: RUF100, SIM113
        sum += number
    mean = sum / count

    return(round(mean,2))

def display_numbers(numbers:list[int]):
    for number in numbers:
        print(f'{numbers.index(number)}: {number} ')

print(f'Minimum to: {minimum(numbers)}')
print(f'Maksimum to: {maximum(numbers)}')
print(f'Średnia to: {mean(numbers)}')
display_numbers(numbers)

    
