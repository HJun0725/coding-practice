def solution(money):
    return [money//5500, money%5500]

'''
새롭게 알게 된 것 - return divmod(money, 5500)
divmod 함수는 (나누어지는 값, 나누는 값)를 인자값으로 받아
몫과 나머지를 튜플로 반환함.
'''