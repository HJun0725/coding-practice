def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5] 
    pattern3 = [3,3,1,1,2,2,4,4,5,5] 
    
    answer = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == pattern1[i%5]:
            answer[0] += 1
        if answers[i] == pattern2[i%8]:
            answer[1] += 1
        if answers[i] == pattern3[i%10]:
            answer[2] += 1
            
    result = []
    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i+1)
    return result