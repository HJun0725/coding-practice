def solution(spell, dic):
    for i in dic:
        if len(i) == len(spell):
            if set(spell) == set(i):
                return 1
    return 2