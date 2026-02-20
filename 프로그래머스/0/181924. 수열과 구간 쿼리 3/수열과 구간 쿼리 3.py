def solution(arr, queries):
    s = 0
    for i,j in queries:
        s = arr[i]
        arr[i] = arr[j]
        arr[j] = s
        
    return arr