def solution(picture, k):
    answer = []
    for i in picture:
        for _ in range(k):
            answer.append(''.join(j*k for j in i))
    return answer