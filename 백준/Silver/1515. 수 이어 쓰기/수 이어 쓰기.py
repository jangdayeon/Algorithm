n = list(map(int, list(input())))
a = 1 #리턴할 값
idx = 0 # n의 인덱스
while True:
    if(idx == len(n)):
        break
    aa = list(map(int, list(str(a))))
    for i in aa:
        if(idx == len(n)):
            break
        if (i == n[idx]):
            idx += 1
    a+=1
print(a-1)