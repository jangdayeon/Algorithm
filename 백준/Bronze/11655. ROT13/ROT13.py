a = list(input())
b = ""
for i in a :
    if(ord(i)>=ord('A') and ord(i)<=ord('Z')):
        if(ord(i)>=ord('A')+13):
            b+=(chr(ord(i)-13))
        else:
            b+=(chr(ord(i)+13))
    elif(ord(i)>=ord('a') and ord(i)<=ord('z')):
        if(ord(i)>=ord('a')+13):
            b+=(chr(ord(i)-13))
        else:
            b+=(chr(ord(i)+13))
    else:
        b+=(i)
print(b)