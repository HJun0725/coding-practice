def solution(before, after):
    answer = 0
    beforeBoW = {}
    afterBoW = {}
    
    for i in before:
        if i in beforeBoW:
            beforeBoW[i] += 1
        else:
            beforeBoW[i] = 1
    
    for i in after:
        if i in afterBoW:
            afterBoW[i] += 1
        else:
            afterBoW[i] = 1
            
    if afterBoW == beforeBoW:
        return 1
    else:
        return 0