def solution(numLog):
    answer = []
    for i in range(1, len(numLog)):
        op = numLog[i] - numLog[i-1]
        if op == 1:
            answer.append("w")
        elif op == -1:
            answer.append("s")
        elif op == 10:
            answer.append("d")
        elif op == -10:
            answer.append("a")
    return ''.join(answer)