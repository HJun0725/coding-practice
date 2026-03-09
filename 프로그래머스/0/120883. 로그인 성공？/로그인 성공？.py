def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw == i:
            return "login"
        elif id_pw[0] in i:
            answer = "wrong pw"
    return "fail" if answer == '' else answer