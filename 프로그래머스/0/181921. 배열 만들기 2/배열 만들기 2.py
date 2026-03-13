def solution(l, r):
    max_num = "1000000"
    answer = [5 * int(bin(i)[2:]) for i in range(1, 2**len(max_num)+1) if l <= 5 * int(bin(i)[2:]) <= r]
    return [-1] if answer == [] else answer