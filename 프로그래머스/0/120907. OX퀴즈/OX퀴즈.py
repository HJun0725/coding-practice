def solution(quiz):
    answer = []
    for i in quiz:
        x, y = i.split("=")
        if eval(x) == int(y):
            answer.append("O")
        else:
            answer.append("X")
    return answer