import sys
input = sys.stdin.readline

checkStr = "UCPC"
checkList = [ ch for ch in checkStr ]

have_to_check = input().rstrip()

for ch in have_to_check:
    if len(checkList) <= 0:
        break
    if ch == checkList[0]:
        checkList.pop(0)

if len(checkList) >= 1:
    print("I hate UCPC")
else:
    print("I love UCPC")