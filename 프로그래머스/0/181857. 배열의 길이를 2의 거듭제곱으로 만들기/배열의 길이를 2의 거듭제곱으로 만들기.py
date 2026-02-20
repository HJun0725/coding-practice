def solution(arr):
    while len(arr) != 2**(len(bin(len(arr)))-3): 
        arr.append(0)
    return arr