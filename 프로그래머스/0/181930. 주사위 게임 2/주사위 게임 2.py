def solution(a, b, c):
    answer = 1
    num = int(a==b and b==c and c==a) + int(a==b or b==c or c==a) + 1
    
    for i in range(1, num+1):
        answer *= a**i + b**i + c**i
        
    return answer
        

