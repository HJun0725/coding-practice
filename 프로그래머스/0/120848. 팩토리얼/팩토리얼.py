def solution(n):
    i = 1
    cnt = 1
    while i <= n:
        i *= cnt+1
        cnt += 1
    return cnt-1