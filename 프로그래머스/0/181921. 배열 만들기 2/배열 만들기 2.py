def solution(l, r):
    max_num = "1000000"
    zero_five = [5 * int(bin(i)[2:]) for i in range(1, 2**len(max_num)+1)]
    answer = [i for i in zero_five if l <= i <= r]
    return [-1] if answer == [] else answer