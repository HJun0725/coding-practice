def solution(slice, n):
    answer = 1
    a = slice
    while n > slice:
        slice += a
        answer += 1
    return answer