def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        min_num = 1000000
        for idx in range(s,e+1):
            if arr[idx] < min_num and arr[idx] > k:
                min_num = arr[idx]
        if min_num != 1000000:
            answer.append(min_num)
        else: 
            answer.append(-1)
    return answer