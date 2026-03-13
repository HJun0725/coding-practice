def solution(A, B):
    answer = A * 2
    for i in range(len(A)):
        if answer[len(A)-i:len(answer)-i] == B:
            return i
    return -1