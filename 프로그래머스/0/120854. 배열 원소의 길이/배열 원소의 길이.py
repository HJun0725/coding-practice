def solution(strlist):
    return [len(i) for i in strlist]

'''
새롭게 알게 된 것 - return list(map(len, strlist))
map 함수는 (변환 함수, 반복 가능 객체)를 인자값으로 받아
객체의 각 요소를 함수를 통해 변환된 값을 반환한다.
'''