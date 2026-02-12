def solution(board, k):
    answer = 0
    for i in board[:k+1]:
        for j in range(len(i)):
            if j <= k:
                answer += i[j]
        k -= 1
    return answer