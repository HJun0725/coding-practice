def solution(polynomial):
    p = polynomial.split()
    v = []
    n = []
    for i in range(0,len(p),2):
        if "x" in p[i]:
            if p[i] == "x":
                v.append(1)
            else:
                v.append(int(p[i].replace("x","")))
        else:
            n.append(int(p[i]))
            
    if sum(v) == 1:
        if n == []:
            return "x"
        else:
            return f"x + {sum(n)}"
    else:
        if n == [] or v == []:
            return [f"{sum(v)}x",f"{sum(n)}"][int(n != [])]
        else:
            return f"{sum(v)}x + {sum(n)}"