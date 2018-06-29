f=[[0,0,0,1,0,0],[0,0,1,0,0,0],[0,0,1,1,0,0],[0,1,0,0,0,0],[0,1,0,1,0,0],
   [0,1,1,0,0,0],[0,1,1,1,0,0],[1,0,0,0,0,0],[1,0,0,1,0,0]]

input_f1 = int(input())
input_f2 = int(input())

count_and = 0
count_or = 0

comp1 = f[input_f1-1]
comp2 = f[input_f2-1]

i = 0
while(i <= 5):
    if comp1[i] == 1 and comp2[i] == 1:

        count_and += 1

    if comp1[i] == 1 or comp2[i] == 1:
        count_or += 1

    i += 1

print(count_and)
print(count_or)