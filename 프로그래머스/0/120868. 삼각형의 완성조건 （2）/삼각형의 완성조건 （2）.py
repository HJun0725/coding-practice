def solution(sides): 
    answer = sum(1 for i in range(max(sides)-min(sides)+1, max(sides))) + sum(1 for i in range(max(sides),sum(sides)))
    return answer