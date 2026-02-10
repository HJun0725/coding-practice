def solution(lines):
    answer = []
    for idx,(s1,e1) in enumerate(lines):
        for s2,e2 in lines[idx+1:]:
            l = []
            for i in range(s2,e2):
                if s1 <= i < e1:
                    l.append(i)
            answer.append(l)
    answer = set(j for i in answer for j in i)
    return len(answer)