import sys

points:int = int(input("Points: "))

def assign_grade(points:int)->tuple[float,str]:
        if points > 100 or points < 0:
            print("Error: points out of range")
            sys.exit()
        elif points >= 0 and points <= 49:
            return((2.0,"ndst"))
        elif points >= 50 and points <= 59:
            return((3.0, "dst"))
        elif points >= 60 and points <= 69:
            return((3.5, "dst plus"))
        elif points >= 70 and points <= 79:
            return((4.0, "db"))
        elif points >= 80 and points <= 89:
            return((4.5, "db plus"))
        else:
            return((5.0, "bdb"))

grade:tuple[float,str] = assign_grade(points)

print(f"{grade[1]} ({grade[0]})")

        
