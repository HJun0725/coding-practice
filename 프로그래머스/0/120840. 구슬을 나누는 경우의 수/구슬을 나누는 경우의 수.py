def getFactorial(n):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p

def solution(balls, share):
    return getFactorial(balls)/(getFactorial(balls-share)*getFactorial(share))