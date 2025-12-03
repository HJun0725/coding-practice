def solution(n):
    answer = 0
    count = 0
    
    a = n
    b = n
    
    for i in range(1, n + 1):
        if a % 2 != 0:
            count += 1
        a = a // 2
        
        if a == 0:
                break
        
        
    for i in range(1, b + 1):
        biggerCount = 0
        b = n + i
        for _ in range(1, b + 1):
            if b % 2 != 0:
                biggerCount += 1
            b = b // 2
            
            if b == 0:
                break
            
        if biggerCount == count:
            answer = n + i
            break
    
       
    return answer