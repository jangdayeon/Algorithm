n =int(input())

x = [0] * (n+1)

a = 1 # 제곱수인지 확인하는 값
cnt = 0 #x에 입력할 값
chk = []
for i in range(1,n+1):
    if(i==a**2):
        chk = [i**2 for i in range(1,a+1)] # 1, 4, 9 등 저장
        x[i] = 1
        a += 1
    else:
        c = list(map(lambda w: x[i-w], chk)) # 1,4,9를 뺐을 때의 인덱스
        m = min(c)
        x[i] = m + 1
print(x[n])