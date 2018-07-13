import random

game_data = {1:'scissor', 2:'rock', 3: 'paper'}
win_cnt = 0 #ㅇㅣ긴 횟수

while(win_cnt<2):
    print("input your number")
    user = int(input())
    comp = random.randint(1,3)

    print(game_data[user],game_data[comp])

    if user == 1:
        comp = comp % 3
    if comp == 1:
        user = user % 3

    if user == comp:
        print("draw")
    elif user > comp:
        print("you win")
        win_cnt += 1
    elif user < comp:
        print("you lose")