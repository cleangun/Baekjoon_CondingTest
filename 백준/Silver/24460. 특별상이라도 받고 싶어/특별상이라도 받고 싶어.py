import sys
input = sys.stdin.readline
    
# 첫 번째 방법 -- 내가 작성  ( long runtime )
    
# def find_price(graph, length):
#     if length <= 1:
#         return graph[0][0]
    
#     one = find_price([ row[:length//2] for row in graph[:length//2] ] ,length//2)
#     two = find_price([ row[length//2:] for row in graph[:length//2] ] ,length//2)
#     three = find_price([ row[:length//2] for row in graph[length//2:] ] ,length//2)
#     four = find_price([ row[length//2:] for row in graph[length//2:] ] ,length//2)
    
#     lst = [one,two,three,four]
#     lst.pop(lst.index(min(lst)))
#     return min(lst)

# 두 번째 방법 -- 참고 답안 (short runtime)
# 4부분의 root 시작 점들을 recursion에 넘겨서 length로 사각형의 크기를 인식함
def find_price(x,y,length):
    if length <= 1:
        return graph[x][y]

    left_top = find_price(x,y,length // 2)
    right_top = find_price(x+length//2,y,length//2)
    left_bottom = find_price(x,y+length//2, length//2)
    right_bottom = find_price(x+length//2, y+length//2, length//2)
    
    result = [left_top, right_top,left_bottom,right_bottom]
    result.sort()
    return result[1]

if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append( [ int(digit) for digit in input().rstrip().split() ] )
    #print(find_price(graph,n)) -- 첫 번째 방법
    print(find_price(0,0,n))    # -- 두 번째 방법

    
