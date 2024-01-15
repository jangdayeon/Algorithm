a = list(input().strip())
a.sort()
s = 0
where =0
for i in a:
    if(ord(i)>=ord('A')):
        where = a.index(i)
        break
    else:
        s += int(i)

for i in range(where,len(a)):
    print(a[i], end='')
print(s, sep='')