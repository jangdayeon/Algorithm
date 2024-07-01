def solution(citations):
    for ch in range(max(citations),-1,-1): #ch = 인용 횟수
        more = 0 #h번 이상 인용된 논문
        for c in citations:
            if c>=ch:
                more += 1
        if more >= ch and len(citations)-more <= ch:
            return ch