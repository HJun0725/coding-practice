def solution(arr, k):
    a = []
    for i in arr:
        if i not in a:
            a.append(i)
    return a[:k] if len(a) >= k else a + [-1 for _ in range(k-len(a))]