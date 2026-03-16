def solution(sizes):
    max_wh = max(sizes[0])
    min_wh = min(sizes[0])
    for i in sizes:
        if max_wh < max(i):
            max_wh = max(i)
        if min_wh < min(i):
            min_wh = min(i)
    return max_wh * min_wh