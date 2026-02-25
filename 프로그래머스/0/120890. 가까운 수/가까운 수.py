def solution(array, n):
    l = [abs(n-i) for i in array]
    cnt = [i for i in array if abs(n-i) == min(l)]
    return min(cnt)