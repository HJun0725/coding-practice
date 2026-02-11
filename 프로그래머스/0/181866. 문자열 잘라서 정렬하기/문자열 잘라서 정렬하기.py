def solution(myString):
    answer = sorted(myString.split("x"))
    return answer if "" not in answer else [i for i in answer if i != ""]