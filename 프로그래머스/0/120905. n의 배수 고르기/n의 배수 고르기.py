def solution(n, numlist):
    return [i for i in numlist if i%n == 0]

'''
새롭게 알게 된 것 - return list(filter(lambda v: v%n==0, numlist))
filter 함수는 인자 값으로 (True/False 반환 함수, 반복 가능 객체)를 받아
객체의 요소에서 True 값만 반환한다.
'''