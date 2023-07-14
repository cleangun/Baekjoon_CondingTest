import sys
input = sys.stdin.readline

n = int(input())
numlst = []
for _ in range(n):
    numlst.append(int(input()))

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    l = r = 0
    merged = []
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            merged.append(left_arr[l])
            l += 1
        elif left_arr[l] > right_arr[r]:
            merged.append(right_arr[r])
            r += 1
        else:
            merged.append(left_arr[l])
            merged.append(right_arr[r])
            l += 1; r += 1
    merged += left_arr[l:]
    merged += right_arr[r:]
    return merged

for num in merge_sort(numlst):
    print(num)