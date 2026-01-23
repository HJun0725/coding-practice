def solution(my_string, letter):
    return ''.join([i for i in my_string if i != letter])

'''
새롭게 알게 된 것 - return my_string.replace(letter, '')
replace 함수는 인자값으로 (수정할 문자, 수정 내용)을 받아 
수정된 문자열을 리턴
'''