li = []
cnt = 0
n = int(input())
i = 1
while True:
    i +=1
    if(str(i).find('666')!= -1):
        li.append(i)
        cnt +=1
        if (cnt == n):
            break
print(li[n-1])