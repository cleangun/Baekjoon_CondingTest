import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append([ int(i) for i in input().rstrip().split() ])
    
resultList = [0]*3 # 0번 0 , 1번 1, 2번 -1
def isSameBox(graph):
    # 2차원 배열일 경우에만 사용가능합니다
    cnt = 0
    for i in graph:
        cnt += i.count(graph[0][0])
    return cnt

def count_paper(graph,length):
    if isSameBox(graph) == length**2:
        resultList[graph[0][0]] += 1
        return
    if length == 1:
        resultList[graph[0][0]] += 1
        return
    divisor = length // 3
    for y in range(length // divisor):
        for x in range(length // divisor):
            count_paper([ xline[x*divisor:(x+1)*divisor] for xline in \
                graph[y*divisor:(y+1)*divisor]], length//3)
    return
count_paper(graph,n) # 0번 : 0 , 1번 : 1 , 2번 : -1
resultList.insert(0,resultList.pop(-1))
print(*resultList)