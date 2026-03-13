def solution(a, b):
    div_b = []
    
    for i in range(2, int(b**0.5)+1):
        if b%i == 0:
            while b%i == 0:
                b //= i
                div_b.append(i)
    div_b.append(b)

    for i in div_b[:]:
        print(a%i)
        if a%i == 0:
            a //= i
            div_b.remove(i)
    
    if div_b == []:
        return 1
    
    for i in div_b:
        if i != 2 and i != 5:
            return 2
    return 1