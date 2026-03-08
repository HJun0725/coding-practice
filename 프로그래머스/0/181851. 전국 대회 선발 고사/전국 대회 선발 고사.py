def solution(rank, attendance):
    l = [rank[i] if attendance[i] else 101 for i in range(len(rank))]
    r = sorted(l)
    return sum((10000//100**i)*l.index(r[i]) for i in range(3))