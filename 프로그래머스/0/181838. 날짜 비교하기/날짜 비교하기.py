def solution(date1, date2):
    for i in range(len(date1)):
        if date1 < date2:
            return 1
    return 0