def solution(myString):
    answer = ''
    for i in myString:
        if ord('A') <= ord(i) <= ord('Z'):
            answer += i
        else:
            answer += chr(ord(i)-32)
    return answer

'''
함수 사용
def solution(myString):
    return answer.upper()
'''