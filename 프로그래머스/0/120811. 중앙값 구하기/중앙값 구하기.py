def solution(array):
    array.sort()
    return array[len(array)//2]

'''
새롭게 알게 된 것
sort 이외에도 sorted 사용해서 기존 객체를 건들이지 않고 
바로 연산에 활용 가능
'''