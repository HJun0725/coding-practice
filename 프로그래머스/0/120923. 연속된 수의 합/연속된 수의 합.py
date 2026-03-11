def solution(num, total):
    answer = []
    t = total
    if total == 0:
        return [i for i in range(-num//2+1, num//2+1)]
    while sum(answer) != total:
        answer = []
        for i in range(t, t-num, -1):
            answer.append(i)
        t -= 1
    return sorted(answer)