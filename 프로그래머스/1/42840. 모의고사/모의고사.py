def solution(answers):
    p0 = [1,2,3,4,5]
    p1 = [2,1,2,3,2,4,2,5]
    p2 = [3,3,1,1,2,2,4,4,5,5]
    correct = [0,0,0] #차례대로 p0,p1,p2
    for i,a in enumerate(answers): #정답 유무 확인
        if a == p0[i%5]:
            correct[0]+=1
        if a == p1[i%8]:
            correct[1]+=1
        if a == p2[i%10]:
            correct[2]+=1
    
    answer = [] #가장 많이 맞춘 사람을 담을 리스트
    for i,c in enumerate(correct): #가장 많이 맞춘 사람 answer 리스트에 추가
        if c == max(correct):
            answer.append(i+1)
    return answer