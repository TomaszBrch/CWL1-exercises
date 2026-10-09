import sys

a = int(input('a: '))
b = int(input('b: '))

if not a <= b :
    print("Error: invalid input")
    sys.exit()

for i in range(a, b+1):
    if i/2 != i//2:
        print(i, end=" ")
    else:
        continue
print('\n')
for i in range(a, b+1):
    if i/3 == i//3:
        print(i, end=" ")
    else:
        continue

