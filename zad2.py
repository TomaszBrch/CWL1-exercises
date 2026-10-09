import sys

a : int = int(input("a: "))
b : int = int(input("b: "))

znak : str = str(input("znak: "))

def calculate(a:int,b:int, znak:str)->float:
    if znak == "+":
        return(a+b)
    elif znak == "-":
        return(a-b)
    elif znak == "*":
        return(a*b)
    elif znak == "/":
        return(a/b)
    elif znak == "//":
        return(a//b)
    elif znak == "%":
        return(a%b)
    elif znak == "**":
        return float(a) ** b
    else:
        print("Error: unknown operator")
        sys.exit()
try:
    wynik = calculate(a,b,znak)
except ZeroDivisionError:
    print("Error: division by zero")
    sys.exit()


print(f"{a} {znak} {b} = {wynik}")




    
