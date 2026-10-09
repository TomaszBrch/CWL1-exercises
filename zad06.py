import sys


def factorial_iter(n:int)->int:
    '''
    Funkcja dla liczby całkowitej n zwraca n! 
    za pomocą iteracji
    '''

    if n < 0 :
        print("Error: invalid input")
        sys.exit()

    res = 1
    
    for i in range(1,n+1):
        res *= i

    return(res)
def fibonacci_iter(n:int)->int:
    '''
    Funkcja dla liczby całkowitej n zwraca n-ty wyraz ciągu fibonacciego
    za pomocą iteracji
    '''
    if n < 0 :
        print("Error: invalid input")
        sys.exit()
    a = 1
    b = 1
    for _ in range(1, n-1):

        c = b
        b = a + b
        a = c
    return(b)
def gdc_iter(n1:int, n2: int)->int:
    '''
    Funkcja dla całkowitych n1 i n2 zwraca ich największy wspólny dzielnik (NWD)
    za pomocą iteracji
    '''

    if n1 < 0 or n2 < 0:
        print("Error: invalid input")
        sys.exit()
    if n1 == 0:
        return(n1)
    elif n2 == 0:
        return(n2)

    while n1 != n2:
        if n1 > n2:
            n1 -= n2
        elif n1 < n2:
            n2 -= n1
    return(n1)
def factorial_reku(n:int)->int:
    '''
    Funkcja dla liczby całkowitej n zwraca n!
    za pomocą rekurencji
    '''

    if n < 0:
        print("Error: invalid input")
        sys.exit()
    if n == 0:
        return(1)
    else:
        return n * factorial_reku(n-1)
def fibonacci_reku(n:int)->int:
    '''
    Funkcja dla liczby całkowitej n zwraca n-ty wyraz ciągu fibonacciego
    za pomocą rekurencji
    '''

    if n < 0:
        print("Error:Invalid input")
        sys.exit()

    if n <= 1:
        return(n)
    else:
        return(fibonacci_reku(n-1)+fibonacci_reku(n-2))
def gcd_reku(n1:int, n2:int)->int:
    '''
    Funkcja dla całkowitych n1 i n2 zwraca ich największy wspólny dzielnik (NWD)
    za pomocą rekurencji
    '''
    if n1 < 0 or n2 < 0:
        print("Error: invalid input")
        sys.exit()
    if n1 == 0:
        return(n1)
    elif n2 == 0:
        return(n2)
    if n1 == n2:
        return n1
    elif n1 > n2:
        return gcd_reku(n1-n2, n2)
    else:
        return gcd_reku(n1, n2-n1)

        





    
        

