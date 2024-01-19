import sys
input = sys.stdin.readline

T = int(input()) #테스트 케이스 수
whitch = [[-1,1],[0,1],[1,1]]
for _ in range(T):
    n,m = map(int, input().split()) #n * m 의 금광 (n이 깊이)
    guang = [0] * n
    g = list(map(int, input().split()))
    j = 0
    for i in range(0,len(g),m):
        guang[j] = g[i:i+m]
        j+=1

    for x in range(1,m):
        for z in range(n):
            chk = []
            for k in [-1,0,1]:
                if(z+k>-1 and z+k<n):
                    chk.append(guang[z+k][x-1])
            ma = max(chk)
            
            guang[z][x] +=ma

    rst = list(map(lambda x:x[m-1], guang))
    print(max(rst))

