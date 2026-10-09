a : int = int(input("a: "))
b : int = int(input("b: "))

if not a >= b:
    print("Error: invalid input")

for i in range(b,a+1):
    for j in range(b,a+1):
        print(f"{i} * {j} = {i*j}")