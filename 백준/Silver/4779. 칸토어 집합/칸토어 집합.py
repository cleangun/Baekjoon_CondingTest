import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        arr = "-" * (3**n)

        def split_func(arr):
            if len(arr) == 1:
                return arr
            
            length = len(arr) // 3
            mid = length
            
            return split_func(arr[0:mid]) + (" "*length) + split_func(arr[(mid+mid):len(arr)])
        print(split_func(arr))
    except:
        break