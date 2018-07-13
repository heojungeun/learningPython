import sys


with open("test.txt",'w+') as f:
    for i in range(1,10):
        data = "%d lines\n" % i
        f.write(data)
    f.seek(0,0)
    num = int(input())
    lines = f.readlines()
    print(lines[num-1], end='')


