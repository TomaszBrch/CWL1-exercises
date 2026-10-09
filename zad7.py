numbers = [4, 8, 15, 16, 23, 48]

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
        

    
