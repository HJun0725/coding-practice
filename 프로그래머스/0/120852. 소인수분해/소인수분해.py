def solution(n):
    i = 2
    cnt = 0
    answer = []
    while n != 1:
        if n%i == 0:
            cnt += 1
            n //= i  
        elif cnt >= 1 and n%i != 0:
            answer.append(i)
            i += 1
            cnt = 0
        else:
            i += 1
    return answer + [i]