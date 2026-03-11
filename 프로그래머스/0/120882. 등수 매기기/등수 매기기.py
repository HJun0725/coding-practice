def solution(score):
    avg = [sum(i)/2 for i in score]
    sortedAvg = sorted(avg)[::-1]
    return [sortedAvg.index(avg[i])+1 for i in range(len(avg))]