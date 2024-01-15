import sys
input = sys.stdin.readline

text = input().strip()
text=text.upper()

dupClear = list(set(text))

maxCnt = max(text.count(dupClear[i]) for i in range(len(dupClear)))
isitOne= 0
oneText = ''
for i in range(len(dupClear)):
    if(text.count(dupClear[i])==maxCnt):
        isitOne+=1
        oneText=dupClear[i]
        
if(isitOne>1):
    print('?')
else:
    print(oneText)