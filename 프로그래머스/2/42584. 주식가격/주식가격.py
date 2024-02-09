def solution(prices):
    answer = []
    for i in range(len(prices)):
        a = prices[i]
        if(i == len(prices)-1):
            answer.append(0)
        else:
            b = 100000
            whereB = -1
            for j in range(i+1,len(prices)):
                if(prices[j]<a):
                    b = prices[j]
                    whereB = j
                    break
            if (a>b):
                answer.append(whereB-i)
                # print(b, "index = ", whereB)
            else:
                answer.append(len(prices)-i-1)
    return answer