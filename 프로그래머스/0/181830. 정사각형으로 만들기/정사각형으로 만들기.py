def solution(arr):
    if len(arr) == len(arr[0]):
        return arr
        
    else:
        if len(arr) > len(arr[0]):#열이 행보다 길 때
            for i in range(len(arr)):
                for _ in range(len(arr)-len(arr[i])):   
                    arr[i].append(0)
        else: 
            for i in range(len(arr[0])-len(arr)):
                arr.append([0]*len(arr[0]))

    return arr