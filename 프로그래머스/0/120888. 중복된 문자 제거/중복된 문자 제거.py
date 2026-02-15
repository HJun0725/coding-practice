def solution(my_string):
    answer = ''
    d = []
    for i in my_string:
        if i not in d:
            answer += i
            d.append(i)
    return answer
        