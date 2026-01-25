def solution(my_string, n):
    return ''.join([my_string[i] for i in range(-1, -n-1, -1)])[::-1]