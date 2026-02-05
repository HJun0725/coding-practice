def solution(arr):
    answer = []
    for i in arr:
        answer += [i] * i
    return answer

'''
메모리 효율은 '+='보다 append()가 좋다.
'''