def solution(emergency):
    answer = [i for i in emergency]
    l = sorted(emergency)[::-1]
    for i in range(1, len(l)+1):
        answer[emergency.index(l[i-1])] = i
    return answer