def solution(a, b, c, d):
    num = [a, b, c, d]
    cnt = [num.count(i) for i in num]
    maxCnt = max(cnt)
    
    if maxCnt == 4:
        return 1111*a
    if maxCnt == 3:
        return (10*num[cnt.index(3)]+num[cnt.index(1)])**2
    if maxCnt == 2:
        if min(cnt) == 2:
            if a == b:
                return (a + c) * abs(a - c)
            else:
                return (a + b) * abs(a - b)
        else:
            mul = 1
            for i in num:
                mul *= i
            return mul//(num[cnt.index(2)]**2)
    return min(num)