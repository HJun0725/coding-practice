def solution(my_string):
    return ''.join([i.upper() if i.islower() else i.lower() for i in my_string ])

'''
새롭게 알게 된 것 - return my_string.swapcase()
대문자는 소문자로, 소문자는 대문자로 변환된 문자열을 리턴
'''