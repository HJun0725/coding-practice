def solution(n):
    answer = [[]]    
    
    for i in range(n):
        if i == 0:
            for _ in range(n):
                answer[i].append(0)
        else:
            answer.append([])
            for _ in range(n):
                answer[i].append(0)
        
    for i in range(n):
        for j in range(n - 2 * i):
            if answer[i][j + i] == 0:
                answer[i][j + i] = 4 * i * (n - 1 * i) + j + 1 
                
            if answer[j + i][-i - 1] == 0:
                answer[j + i][-i - 1] = 4 * i * (n - 1 * i ) + n + j - 2 * i
                
            if answer[-i - 1][-j - i - 1] == 0:
                answer[-i - 1][-j - i - 1] = 4 * i * (n - 1 * i ) + 2 * n - 1 + j - 4 * i
                
            if answer[-j - i - 1][i] == 0:
                answer[-j - i - 1][i] = 4 * i * (n - 1 * i ) + 3 * n - 2 + j  - 6 * i
    return answer