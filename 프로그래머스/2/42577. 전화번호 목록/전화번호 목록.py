def solution(phone_book):
    answer = True
    t = sorted(set(map(len, phone_book)))
    
    hs = {}
    for i in sorted(phone_book, reverse=True):
        hs[i] = i
    
    for num in hs:
        for l in t:
            if hs.get(hs[num][:l], num) != num:
                return False
    return True