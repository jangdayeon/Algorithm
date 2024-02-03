n = int(input())
a = [[None] for i in range(n)]
for i in a:
    i.remove(None)
li = list(map(int, input().split()))
for i in range(n):
    if li[i]==-1:
        continue
    else:
        a[li[i]].append(i) #부모에 자식 넣기
        for j in a:
            if (j.count(li[i])!=0): #부모의 부모 찾기
                j.append(i) #할머니랑 손자 연결해주기
for i in range(n):
    for j in a[i]:
        for k in a[j]:
            if (a[i].count(k) ==0):
                a[i].append(k)
#여기까지 각 노드가 저장되어 있는 a에 연결된 것들을 입력
d = int(input())
mustDel = a[d].copy()

mustDel.append(d)
for i in a:
    for j in mustDel:
        if (i.count(j)!=0):
            i.remove(j)
for i in mustDel:
    a[i] = []
    a[i].append(-100) #없는 노드 표시를 위해
rst = 0
for i in a:
    if(len(i)==0):
        rst+=1
print(rst)