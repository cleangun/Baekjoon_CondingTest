import sys
input = sys.stdin.readline

n = int(input())
unsorted_list = list(map(int, input().rstrip().split()))
s = int(input())

large_list = sorted(unsorted_list, reverse=True)

place_idx = 0
large_turn_idx = 0
while place_idx < len(unsorted_list) and s>0:
    for large_turn_idx in range(len(large_list)):
        if s <= 0:
            print(*unsorted_list)
            exit(0)
        idx = unsorted_list.index(large_list[large_turn_idx])
        move = idx - place_idx
        if idx > place_idx and (move <= s) and (unsorted_list[place_idx] < unsorted_list[idx]):
            num = unsorted_list[idx]
            s -= move
            unsorted_list.remove(num)
            unsorted_list.insert(place_idx,num)
            break
    place_idx += 1
print(*unsorted_list)