def solution(bin1, bin2):
    maxLen = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(maxLen)
    bin2 = bin2.zfill(maxLen)
    
    result = []
    cnt = 0
    
    for i in range(maxLen-1, -1, -1):
        result.insert(0, int(bin1[i])+int(bin2[i])+cnt)
        cnt = 0
        if result[0] > 1:
            result[0] %= 2
            cnt += 1
    
    if cnt == 1:
        result.insert(0, 1)
        
    return ''.join(map(str,result))