n = int(input())
a = [str(i) for i in range(0,n+1)]
b = [str(i) for i in range(0, 60)]

rst =0
for i in a:
    for j in b:
        for k in b:
            if(i.count('3')>0 or j.count('3')>0 or k.count('3')>0):
                rst+=1
print(rst)