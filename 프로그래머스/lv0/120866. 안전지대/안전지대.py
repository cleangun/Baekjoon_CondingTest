def solution(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 1:
                dx = [1,1,1,0,0,-1,-1,-1]
                dy = [0,-1,1,-1,1,0,-1,1]
                for i in range(len(dx)):
                    targetx = x + dx[i]; targety = y + dy[i]
                    if ((0 <= targetx) and targetx < len(board[y])) and \
                    (0 <= targety and targety < len(board)) and \
                    board[targety][targetx] != (1 or 2):
                        board[y+dy[i]][x+dx[i]] = 2
    answer = 0
    for line in board:
        answer += line.count(0)
    return answer