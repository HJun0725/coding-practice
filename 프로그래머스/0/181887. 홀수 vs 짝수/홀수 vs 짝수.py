def solution(num_list):
    return max(sum([num_list[i] for i in range(0 ,len(num_list), 2)]), sum([num_list[i] for i in range(1, len(num_list), 2)]))

'''
기존 배열을 사용하는 경우에는 슬라이싱
'''