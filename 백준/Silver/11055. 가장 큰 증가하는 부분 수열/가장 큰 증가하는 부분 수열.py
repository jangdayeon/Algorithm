n = int(input())
li = list(map(int, input().split()))
x = [li[0]] * len(li) #부분계산값 저장할 곳
for i in range(1,len(li)):
    m = 0
    for j in range(0,i):
        if(li[j]<li[i]):
            m = max(m, x[j])
    x[i] = m + li[i]
print(max(x))