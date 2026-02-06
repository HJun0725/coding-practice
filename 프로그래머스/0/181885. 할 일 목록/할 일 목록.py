def solution(todo_list, finished):
    return [todo_list[i] for i in range(len(finished)) if finished[i] == False]

'''
새롭게 알게 된 것 - enumerate
enumerate 함수는 반복 가능한 객체를 인자로 받아 
그 객체의 인덱스와 값을 튜플 타입으로 반환함
'''