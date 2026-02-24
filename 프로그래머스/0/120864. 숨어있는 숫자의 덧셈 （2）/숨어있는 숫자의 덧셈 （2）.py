def solution(my_string):
    s = ''
    answer = 0
    my_string += "e"
    for i in my_string:
        if i.isdigit():
            s += i
        if i.isalpha() and s != '':
            answer += int(s)
            s = ''
    return answer