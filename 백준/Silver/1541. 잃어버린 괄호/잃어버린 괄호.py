sik = list(input())
rst = []
chk = False
numChk = False
for i in range(len(sik)):
    if((sik[i]=='-') and chk == True):
        rst.append(')')
        chk = False
    if not (numChk == False and sik[i] == '0'):
        rst.append(sik[i])
        numChk = True
    if(sik[i] == '+' or sik[i] == '-'):
        numChk = False
    if((i == len(sik)-1) and chk == True):
        rst.append(')')
        chk = False
    if(sik[i]=='-' and chk == False):
        rst.append('(')
        chk = True
print(eval(''.join(rst)))