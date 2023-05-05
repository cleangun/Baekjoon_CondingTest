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