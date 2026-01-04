def solution(id_list, report, k):
    answer = []
    
    reportCount = {} #각 id 별 신고 횟수
    newReport = set() #중복을 제거한 report
    suspensionUser = [] #정지된 id
    reportUser = {}
    
    #각 id 별 신고 당한 횟수 저장 dict 초기화
    for i in id_list:
        reportCount[i] = 0

    #유저가 신고한 id
    for i in id_list:
        reportUser[i] = []    
        
    #중복을 제거한 report 선언
    for i in report:
        reporter, user = i.split()
        newReport.add((reporter, user))
    
    #newReport로 누적 신고 구하기
    for reporter, user in newReport:
        reportCount[user] += 1
        reportUser[reporter].append(user)
    
    #이용 정지 메세지 전송 대상 구하기
    for i in reportCount:
        if reportCount[i] >= k:
            suspensionUser.append(i)

    #answer 구하기
    for i in reportUser:
        count = 0
        for j in reportUser[i]:
            if j in suspensionUser:
                count += 1
        answer.append(count)
    return answer