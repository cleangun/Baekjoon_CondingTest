import sys
input = sys.stdin.readline

n = int(input())
lst = [ int(i) for i in input().rstrip().split() ]
max_value = max(lst)
for _ in range(n):
    if (lst[0] * 100) / max_value > 100:
        lst.pop(0);
        lst.append(100)
    else:
        lst.append((lst.pop(0)*100)/max_value)
print(sum(lst) / n)
