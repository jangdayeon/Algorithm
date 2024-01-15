h,m = map(int, input().split())
t = int(input())

if((m+t)<60):
    print(h, (m+t))
else:
    new_h = (m+t)//60
    new_m = (m+t)%60
    if(h+new_h<=23):
        print((h+new_h), new_m)
    else:
        print((h+new_h-24), new_m)