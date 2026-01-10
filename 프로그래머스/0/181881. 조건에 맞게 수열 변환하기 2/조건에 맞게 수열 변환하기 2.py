def solution(arr):
    answer = 0
    while True:
        beforeArr = [i for i in arr]

        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i]//2
            if arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1

        if arr == beforeArr:
            break
        else:
            answer += 1
    
        
    return answer