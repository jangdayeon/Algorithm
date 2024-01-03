import sys
input = sys.stdin.readline

#문자열 to 숫자열
text = input().strip()
number = ""
for i in range(len(text)):
    t = ord(text[i])
    if(t>=ord('A') and t<=ord('C')):
        number+='2'
    elif(t>=ord('D') and t<=ord('F')):
        number+='3'
    elif(t>=ord('G') and t<=ord('I')):
        number+='4'
    elif(t>=ord('J') and t<=ord('L')):
        number+='5'
    elif(t>=ord('M') and t<=ord('O')):
        number+='6'
    elif(t>=ord('P') and t<=ord('S')):
        number+='7'
    elif(t>=ord('T') and t<=ord('V')):
        number+='8'
    elif(t>=ord('W') and t<=ord('Z')):
        number+='9'
    else:
        number+=''
        
#최소 시간 구하기
rst = 0
for i in range(len(number)):
    rst+= int(number[i])+1

print(rst)