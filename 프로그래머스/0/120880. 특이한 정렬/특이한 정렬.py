def solution(numlist, n):
    answer = []
    dist = sorted([abs(n-i) for i in numlist])
    for i in range(len(dist)):
        if dist[i] == dist[i-1]:
            answer.append(n-dist[i])
        else:
            if n+dist[i] in numlist:
                answer.append(n+dist[i])
            else:
                answer.append(abs(dist[i]-n))
    return answer