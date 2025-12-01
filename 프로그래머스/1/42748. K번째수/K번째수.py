def solution(array, commands):
    answer = []
    numSwitch = 0
    for i in commands:
        ar = []
        for j in range(i[0] - 1, i[1]):
            ar.append(array[j])
            
        for _ in range(len(ar) - 1):
            for j in range(len(ar)-1):
                
                if ar[j] > ar[j+1]:
                    numSwitch = ar[j]
                    ar[j] = ar[j+1]
                    ar[j+1] = numSwitch
        answer.append(ar[i[2]-1])
    return answer