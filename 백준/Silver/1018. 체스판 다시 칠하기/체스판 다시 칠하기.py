line1 = list("WBWBWBWB")
line2 = list("BWBWBWBW")

pan1 = [line1,line2,line1,line2,line1,line2,line1,line2]
pan2 = [line2,line1,line2,line1,line2,line1,line2,line1]

smallest = 64
n,m = map(int, input().split()) #n개의 줄에 m개의 행
pan = []
for i in range(n):
    pan.append(list(input()))

def panChk(i,j):
    x = 0
    y = 0
    chk1 = 0
    chk2 = 0
    global smallest
    for a in range(i,i+8):
        for b in range(j,j+8):
            if(pan1[x][y] != pan[a][b]):
                chk1+=1
            if(pan2[x][y] != pan[a][b]):
                chk2+=1
            y +=1
        x +=1
        y=0
    smallest = min(chk1, chk2, smallest)

for i in range(0, n-8+1):
    for j in range(0, m-8+1):
        panChk(i,j)

print(smallest)        
