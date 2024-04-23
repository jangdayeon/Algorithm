def solution(s, n):
    answer = ""
    for char in list(s):
        if(char.isspace()):
            answer+=" "
        elif(char.isupper()):
            answer +=(chr((ord(char)-ord("A")+n)%26+ord("A")))
        else:
            answer +=(chr((ord(char)-ord("a")+n)%26+ord("a")))   
    return answer