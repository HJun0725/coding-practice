def solution(n):
    for i in range(1, n+1):
        if i%3 == 0 or "3" in str(i):
            n += 1
            while n%3 == 0 or "3" in str(n):
                n += 1
    return n