def solution(num_list):
    oddNum = ""
    evenNum = ""
    for i in num_list:
        if i % 2 == 0:
            evenNum += str(i)
        else:
            oddNum += str(i)            
    return int(oddNum) + int(evenNum)