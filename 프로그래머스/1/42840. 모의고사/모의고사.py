def solution(answers):
    a = [1,2,3,4,5] *(len(answers)//5+1)
    b = [2,1,2,3,2,4,2,5] *(len(answers)//8+1)
    c = [3,3,1,1,2,2,4,4,5,5] *(len(answers)//10+1)
    correct = {}
    correct[1] = 0
    correct[2] = 0
    correct[3] = 0
    for i in range(len(answers)):
        if(a[i]==answers[i]):
            correct[1]+=1
        if(b[i]==answers[i]):
            correct[2]+=1
        if(c[i]==answers[i]):
            correct[3]+=1
    answer = []
    a = sorted(correct.items(), key=lambda x:x[1], reverse=True) #이거 꼭 기억하기
    b = list(a[0])
    m = b[1]
    for i,j in a:
        if j == m:
            answer.append(i)
    return answer