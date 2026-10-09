numbers = [4, 8, 15, 16, 23, 1]

def minimum(numbers:list[int])->int:
    
    minim = float('inf')

    for number in numbers:
        if number < minim:  # noqa: PLR1730
            minim = number
    return int(minim)
            
        

    
