def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            return 1
    return 0

'''
for문을 반복할 필요없이 슬라이싱을 통해 최적화 가능
if my_string[-len(is_suffix):] == is_suffix
'''