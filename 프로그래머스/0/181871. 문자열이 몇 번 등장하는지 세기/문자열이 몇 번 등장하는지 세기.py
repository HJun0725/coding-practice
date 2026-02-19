def solution(myString, pat):
    return sum(myString[i:i+len(pat)].count(pat) for i in range(len(myString) - len(pat) + 1))