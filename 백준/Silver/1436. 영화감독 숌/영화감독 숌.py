import sys
input = sys.stdin.readline

n = int(input())
num = 665
while n > 0:
    num += 1
    if str(num).count("6") < 3:
        continue
    for idx in range(len(str(num))-2):
        str_num = str(num)
        if (str_num[idx] == "6") and (str_num[idx+1] == "6") and (str_num[idx+2] == "6"):
            n -= 1
            break
print(num)