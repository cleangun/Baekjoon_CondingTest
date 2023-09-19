import sys
input = sys.stdin.readline

comb = set()
for i in range(102,1000):
    str_num = str(i)
    if str_num.count("0") >= 1:
        continue
    cor = True
    for index in range(2):
        if str_num.count(str_num[index]) >= 2:
            cor = False
            break
    if cor:
        comb.add(i)
    
for _ in range(int(input())):
    next_comb = set()
    target , strike, ball = map(int,input().split())
    for num in comb:
        strike_cnt, ball_cnt = 0 , 0
        for idx in range(3):
            if str(num)[idx] == str(target)[idx]:
                strike_cnt += 1
            elif str(num)[idx] in str(target):
                ball_cnt += 1
        if (strike == strike_cnt) and (ball == ball_cnt):
            next_comb.add(num)
    comb = next_comb.copy()
print(len(comb))