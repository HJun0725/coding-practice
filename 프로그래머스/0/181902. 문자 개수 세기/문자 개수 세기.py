def solution(my_string):
    result = [0] * 52
    for i in list(map(ord, my_string)):
        if i < 97:
            result[i-65] += 1
        else:
            result[i-71] += 1
    return result