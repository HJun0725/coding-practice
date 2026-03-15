def solution(participant, completion):
    hs = {}
    for name in completion:
        if hs.get(name) is None:
            hs[name] = 1
        else:
            hs[name] += 1
    
    for name in participant:
        if hs.get(name) is None or hs[name] <= 0:
            return name
        else:
            hs[name] -= 1
 