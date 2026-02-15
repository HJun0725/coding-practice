def solution(arr, flag):
    x = []
    for i in range(len(flag)):
        if flag[i]:
            for _ in range(arr[i]*2):
                x.append(arr[i])
        else:
            x = x[:len(x)-arr[i]]
            
    return x