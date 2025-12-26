def solution(board):
    answer = 0
    n = len(board)
    mineIndex = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                mineIndex.append((i,j))
    for r,c in mineIndex:
        for i in range(-1, 2):
            rIdx = r + i
            for j in range(-1, 2):
                cIdx = c + j
                if 0 <= rIdx <= n-1 and 0 <= cIdx <= n-1:
                    board[rIdx][cIdx] = 1
    for i in board:
        for j in i:
            if j == 0:
                answer += 1
    return answer