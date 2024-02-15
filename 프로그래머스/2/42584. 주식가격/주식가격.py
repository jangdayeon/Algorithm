#이것도 아이디어가 ,, ㅎㅎ prices 길이가 10만까지 가서 log2N으로 풀었을 줄 알았는데 n2으로도 가능
#정석대로 풀었다.
#첫번째값 이후에 첫번째 값보다 작은 값 발견시 해당 인덱스를 answer에 추가하고 for문을 break하고 다음 인덱스로 넘어가기

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