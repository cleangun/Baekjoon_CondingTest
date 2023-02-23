# 토너먼트 하면서 두 수가 만나는 라운드 찾는 문제
# => 두 선수의 번호를 /2 로 줄여가면서 딱 맞는 순간이 => 해당 라운드
import sys

input = sys.stdin.readline

n, jimin, han = map(int, input().split())
cnt = 1
while True:
    one = int((jimin + 1) / 2)
    two = int((han + 1) / 2)
    if one == two:
        print(cnt)
        exit(0)
    else:
        cnt += 1
    jimin = one
    han = two

