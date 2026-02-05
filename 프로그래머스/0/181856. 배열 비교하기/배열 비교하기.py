def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        return int(len(arr1) > len(arr2)) - int(len(arr2) > len(arr1))
    else:
        return int(sum(arr1) > sum(arr2)) - int(sum(arr2) > sum(arr1))