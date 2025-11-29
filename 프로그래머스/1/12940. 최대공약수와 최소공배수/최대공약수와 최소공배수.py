def solution(n, m):
    chadae = 1
    for i in range(1, m + 1):
        if n % i == 0 and m % i == 0 and i > chadae:
            chadae = i
    chaso = n*m // chadae

    return [chadae, chaso]