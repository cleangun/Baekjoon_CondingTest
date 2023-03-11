# baekjoon 1157 - 단어공부
import sys
input = sys.stdin.readline

word = input().rstrip().upper()
data = set()
result = []

for i in word:
  data.add(i)
datalist = list(data)
for i in datalist:
  result.append(word.count(i))

if result.count(max(result)) != 1:
  print("?")
else:
  print(datalist[result.index(max(result))])