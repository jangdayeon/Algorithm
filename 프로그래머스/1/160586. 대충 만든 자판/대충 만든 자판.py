# 2번 틀림. -1에 대한 처리를 잘못해서
def solution(keymap, targets):
    result = [0] * len(targets)
    for i,t in enumerate(targets):
        for tt in list(t):
            minimum = 101 #가장 적게 키를 입력하는 수는 몇인지 저장
            for k in keymap:
                if list(k).count(tt)>=1:
                    minimum = min(minimum,list(k).index(tt)+1)
            result[i] = result[i]+minimum if minimum != 101 and result[i] != -1 else -1         
    return result