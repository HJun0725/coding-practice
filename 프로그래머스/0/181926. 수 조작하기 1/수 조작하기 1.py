def solution(n, control):
    alph = {"w": 1, "s": -1, "d": 10, "a": -10}
    for i in control:
        n += alph[i]
    return n

'''
새롭게 알게 된 것 - zip()
두 개 이상의 반복 가능한(iterable) 객체를 인자로 받아, 
각 객체의 동일한 인덱스에 위치한 요소들을 튜플로 묶어주는 내장 함수
'''