def solution(arr):
    stk = [arr[0]]
    i = 1
    while i < len(arr):
        if stk and stk[-1] == arr[i]:
            stk = stk[:len(stk)-1]
            i += 1
        else: 
            stk.append(arr[i])
            i += 1
    return [-1] if not stk else stk