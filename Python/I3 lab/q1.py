a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    if a**2 == b**2 + c**2:
        print("Yes")
    else:
        print("No")

if b > a and b > c:
    if b**2 == a**2 + c**2:
        print("Yes")
    else:
        print("No")

if c > a and c > b:
    if c**2 == b**2 + a**2:
        print("Yes")
    else:
        print("No")