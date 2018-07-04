def f1(a,b):
    mult = a * b
    two = mult % 2
    three = mult % 3
    if two == 0 and three == 0:
        return "all"
    elif two == 0 and three != 0:
        return "two"
    elif two !=0 and three == 0:
        return "three"
    elif two != 0 and three != 0:
        return "none"

while True:
    n1 = int(input())
    if n1 == 0:
        break

    n2 = int(input())
    if n2 == 0:
        break

    print(f1(n1, n2))
