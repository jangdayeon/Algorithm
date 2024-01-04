import sys
input = sys.stdin.readline

a,b = map(int,input().split())
rst =""
jin ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while a:
    rst+=str(jin[a%b])
    a = a//b
print(rst[::-1])