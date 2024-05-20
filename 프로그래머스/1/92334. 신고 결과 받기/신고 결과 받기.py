def solution(id_list, report, k):
    suspended = {}
    result = {}
    for id in id_list:
        suspended[id] = 0
        result[id] = 0
        
    report = set(report)
    for re in report :
        fr, to = re.split(" ")
        suspended[to] += 1
        
    for re in report :
        fr, to = re.split(" ")
        if suspended[to] >= k :
            result[fr] += 1
            
    return list(result.values())