import sys
input= sys.stdin.readline

num = [0 for _ in range(10)]

for i in range(10):
    num[i] = int(input())
    
def div(a):
    return a%42
num = list(map(div, num))
num.sort() #sort를 사용하여 시간복잡도 줄이도록 함

rst = 0
i=0
while(i<10):
    turn = 1
    if(num.count(num[i])>1):
        turn = num.count(num[i])
    i+=turn
    rst+=1
    
print(rst)