def solution(wallpaper):
    filePoint = []
    lux = luy = 1000
    rdx = rdy = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                filePoint.append((i,j))
    for x,y in filePoint:
        if  lux > x:
            lux = x
        if luy > y:
            luy = y
        if rdx < x+1:
            rdx = x+1
        if rdy < y+1:
            rdy = y+1

    return [lux, luy, rdx, rdy]