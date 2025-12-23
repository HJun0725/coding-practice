def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        result = ""
        for j in word:
            i = i.replace(j, " ")
        if len(i.strip()) == 0:
            answer += 1

    return answer