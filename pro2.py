input_int = int(input())

#if input_int == 0:


only_small = 10*int(input_int/5)
small = int(input_int/5)
big = 0
minbox = only_small
if input_int % 5 != 0:
    only_small += (input_int % 5) + 5
    small +=1

only_big = 18*int((input_int/10))
if input_int % 10 != 0:
    only_big += (input_int % 10) + 8
    if only_big < only_small:
        small = 0
        big = int(input_int / 10) + 1
        minbox = only_big

mix = 18*int((input_int/10))
if input_int % 10 != 0 and input_int % 10 < 6:
    mix += (input_int % 10) + 5
    if mix < minbox:
        big = int(input_int / 10)
        small = 1
        minbox = mix

print(big)
print(small)
print(minbox)
"""
if only_small < only_big and only_small< mix:
    print("0")
    small = input_int/5
    print(small)
    print(only_small)
elif only_big < only_small and only_big < mix:
    big = input_int / 10
    print(big)
    print("0")
    print(only_big)
elif mix < only_small and mix < only_big:
    big = input_int / 10
    print()
    small = input_int / 5
    print(small)
    print(only_small)
"""