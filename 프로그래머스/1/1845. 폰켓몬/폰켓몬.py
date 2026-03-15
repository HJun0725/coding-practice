def solution(nums):
    l = len(set(nums))
    return len(nums)/2 if l > len(nums)/2 else l