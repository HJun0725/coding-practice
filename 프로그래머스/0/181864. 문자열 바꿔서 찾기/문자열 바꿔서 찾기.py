def solution(myString, pat):
    table = str.maketrans('AB', 'BA')
    pat = pat.translate(table)
    return 1 if pat in myString else 0