def solution(n, lost, reserve):
    l = sorted([i for i in lost if i not in reserve])
    r = sorted([i for i in reserve if i not in lost])
    n = n-len(l)
        
    for i in l:
        if i-1 in r:
            r.remove(i-1)
            n += 1
        elif i+1 in r:
            r.remove(i+1)
            n += 1
    return n