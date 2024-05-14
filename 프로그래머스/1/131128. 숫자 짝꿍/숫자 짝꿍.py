# 세 번 틀림. result를 리스트에서 str로 바꾸기
#네 번 틀림. counter->dict으로 변경 -> 다섯 번 틀림. dict을 사용하지 않고 바로 result에 추가(답 확인함)
#여섯 번 틀림. 설마 int(result) == 0 에서 int 숫자가 너무 크나 싶어 수정함
def solution(X, Y):
    result = "" 
    for i in range(9,-1,-1):
        x = X.count(str(i))
        y = Y.count(str(i))
        result+=(str(i)*min(x,y))
    if result == "" : 
        return "-1"
    else:
        return "0" if len(result) == result.count("0") else result 
    #오름차순 정렬 후 int로 바꾸고 다시 str로 바꿔 "00" 같은 답 해결