def solution(n):
    for i in range(1,n):
        if 6*i % n == 0:
            return i
    return n