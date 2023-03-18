import sys

input = sys.stdin.readline

n, l = map(int, input().split())

start = 0  # 리스트의 시작 인덱스
end = 0  # 리스트의 끝 인덱스
sum_list = 0  # 리스트 내의 숫자들의 합
result = []  # 최종 결과를 저장할 리스트

while start <= end <= n:
    if len(result) >= l:
        break

    # 현재 합이 n과 같거나 더 큰 경우 start를 1 증가시키고 sum_list에서 start번째 값을 빼준다.
    if sum_list >= n:
        sum_list -= start
        start += 1
    # 현재 합이 n보다 작은 경우 end를 1 증가시키고 sum_list에 end번째 값을 더해준다.
    elif sum_list < n:
        end += 1
        sum_list += end

    # 만약 리스트의 길이가 l 이상이고, 합이 n과 같은 경우 결과 리스트에 start부터 end까지의 값을 저장하고 더 이상 계산하지 않는다.
    if len(result) >= l and sum_list == n:
        result = list(range(start, end+1))

if not result:
    print(-1)
else:
    print(' '.join(map(str, result)))