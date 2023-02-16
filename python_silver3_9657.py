# 첫 번째 점화식 쌓기
N = int(input())
arr = [0 for _ in range(1001)]
arr[1] = 'SK'
arr[2] = 'CY'
arr[3] = 'SK'
arr[4] = 'SK'

for i in range(5, N+1):
  if arr[i-1] == 'SK' and arr[i-3] == 'SK' and arr[i-4] == 'SK':
    arr[i] = 'CY'
  else:
    arr[i] = 'SK'

print(arr[N])

# -------------------------------------

# 두 번째 간결한 정답

# if N % 7 == 2 or N % 7 == 0:  
#   print("CY")
# else:
#   print("SK")


# -------------------------------------


# 경우의 수를 뽑는 코드

# def solution(list,target):
#   if sum(list) >= target:
#     if sum(list) == target:
#       print(f"cor list : {list}",end=' ')
#       if len(list) % 2 == 1:
#         print("SK..!")
#       else:
#         print("CY..!")
#     list.pop()
#     return
#   else:
#     for adnum in [4,3,1]:
#       list.append(adnum)
#       solution(list, target)
    
    

# catch = [1,3,4]
# for i in range(1,20):
#   print(f"N = {i}....!!!")
#   for j in [4,3,1]:
#     list = []
#     list.append(j)
#     solution(list,i)
#   print()
#   print()
    