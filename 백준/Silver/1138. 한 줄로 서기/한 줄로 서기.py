import sys
input = sys.stdin.readline

n = int(input())

tall = []#0번 인덱스 : key값, 1번인덱스 : 앞에 큰 사람 수

key = 1
for value in list([int(digit) for digit in input().rstrip().split()]):
    tall.append([key,value])
    key += 1
#예외 처리 모든 수가 0이라면
if tall.count(0) == (n+1):
    for i in range(1,n+1):
        print(i,end=" ")
    exit(0)

tall = sorted(tall, key=lambda x: (x[1],-x[0]))
result = []
for arg in tall:
    key, value = arg
    count = 0
    idx = 0
    if value == 0:
        result.insert(idx,key)
        continue
    while idx <= len(result):
        if count == value:
            result.insert(idx,key)
            break
        if result[idx] > key:
            count += 1
        idx += 1
for i in result:
    print(i,end=" ")