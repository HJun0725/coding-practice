def solution(strings, n):
    for _ in range(len(strings) - 1):
        for i in range(len(strings) - 1):
            if strings[i][n] > strings[i+1][n]:
                strings[i], strings[i+1] = strings[i+1], strings[i]
            elif strings[i][n] == strings[i+1][n]:
                for k in range(min(len(strings[i]), len(strings[i+1]))):
                    if strings[i][k] > strings[i+1][k]:
                        strings[i], strings[i+1] = strings[i+1], strings[i]
                        break
                    elif strings[i][k] < strings[i+1][k]:
                        break
                    elif k+1 == min(len(strings[i]), len(strings[i+1])) and strings[i][k] == strings[i+1][k]:
                        if len(strings[i]) > len(strings[i+1]):
                            strings[i], strings[i+1] = strings[i+1], strings[i]
    return strings