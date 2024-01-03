import sys
input = sys.stdin.readline

text = input().strip()

check = 1
for i in range(0, len(text)//2):
    if(text[i]!=text[len(text)-1-i]):
        check=0
print(check)