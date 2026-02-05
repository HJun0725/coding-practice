def solution(arr, n):
    for i in range(int(len(arr)%2 == 0), len(arr), 2):
        arr[i] += n
    return arr