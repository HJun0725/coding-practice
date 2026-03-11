def solution(array):
    a = list(set(array))
    m = [array.count(i) for i in a]
    return -1 if m.count(max(m)) > 1 else a[m.index(max(m))]