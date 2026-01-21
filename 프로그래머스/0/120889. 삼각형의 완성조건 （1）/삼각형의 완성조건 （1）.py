def solution(sides):
    n = max(sides)
    if n < sum(sides) - n:
        return 1
    else: 
        return 2