import sys

points:int = int(input("Points: "))

def assign_grade(points:int) -> tuple[float,str]:
    match points:      
        case n if n > 100 or n < 0:
            print("Error: points out of range")
            sys.exit()
        case n if n >= 0 and n <= 49:
            return((2.0,"ndst"))
        case n if n >= 50 and n <= 59:
            return((3.0, "dst"))
        case n if n >= 60 and n <= 69:
            return((3.5, "dst plus"))
        case n if n >= 70 and n <= 79:
            return((4.0, "db"))
        case n if n >= 80 and n <= 89:
            return((4.5, "db plus"))
        case n if n >=90 and n <=100:
            return((5.0, "bdb"))
        case _:
            sys.exit()


grade = assign_grade(points)

print(f"{grade[1]} ({grade[0]})")