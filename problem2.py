it = input().split()

print(it)

for i in it[0]:
    if it[0].index(i) != 0:
        print(":", end="")
    print(i, end="")

