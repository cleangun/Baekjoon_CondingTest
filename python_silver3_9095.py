import sys
import itertools
input = sys.stdin.readline

n = int(input())

def count_ways(target):
    result = 0
    for three in range(0,(target//3)+1):
        n = target - (three*3)
        for two in range(0,(n // 2)+1):
            n = (target - (three*3)) - (two*2)
            one = 0 if n <= 0 else n//1
            if (one + (two*2) + (three*3)) == target:
                lst = [1]*one + [2]*two + [3]*three
                permutations = set(itertools.permutations(lst, len(lst)))
                result += len(permutations)
    return result

# main
for _ in range(n):
    target = int(input())
    print(count_ways(target))
    
    
# 제일 좋은 코드 - 서브 Problem으로 나눠서 풀기
# =>
# Baekjoon silver3 9095 - 1,2,3 더하기
# 최고의 효율코드
# import sys

# iuput = sys.stdin.readline
# case = int(input())


# def calc(num):
#   if num == 1:
#     return 1
#   elif num == 2:
#     return 2
#   elif num == 3:
#     return 4
#   else:
#     return calc(num - 3) + calc(num - 2) + calc(num - 1)


# for _ in range(case):
#   n = int(input())
#   print(calc(n))
