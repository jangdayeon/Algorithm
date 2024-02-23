from bisect import bisect_right, bisect_left

def solution(words, queries):
    wordLenList1 = [[] for _ in range (10001)]#그냥 버전
    wordLenList2 = [[] for _ in range (10001)]#reverse된 버전
    for word in words:
        wordLenList1[len(word)].append(word)
        wordLenList2[len(word)].append(word[::-1])
    
    answer = []
    for i in range(10001):
        wordLenList1[i].sort()
        wordLenList2[i].sort()
        
    for query in queries:
        wll1 = wordLenList1[len(query)]
        wll2 = wordLenList2[len(query)]
        if query[0] == "?" :
            q = query[::-1]
            qa = q.replace('?','a')
            qz = q.replace('?','z')
            bl = (bisect_left(wll2, qa))
            br = (bisect_right(wll2, qz))
            answer.append(br-bl)
        else:
            qa = query.replace('?','a')
            qz = query.replace('?','z')
            bl = (bisect_left(wll1, qa))
            br = (bisect_right(wll1, qz))
            answer.append(br-bl)
        
    return answer