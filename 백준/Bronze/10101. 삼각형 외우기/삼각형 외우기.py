import sys
input =sys.stdin.readline

s = []
for i in range(3):
    s.append(int(input()))
if(s[0]+s[1]+s[2]==180):
    if(s[0]==s[1] and s[1]==s[2] and s[2]==s[0]):
        print("Equilateral")
    elif(s[0]==s[1] or s[1]==s[2] or s[2]==s[0]):
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")