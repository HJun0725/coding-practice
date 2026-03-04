def solution(my_string):
    answer = 0
    num = []
    op = ["+"]
    
    for i in my_string.split():
        if i.isdigit():
            num.append(i)
        else:
            op.append(i)
    
    for i in range(len(num)):
        if op[i] == "+":
            answer += int(num[i])
        else:
            answer -= int(num[i])
            
    return answer