def solution(n, words):
    done = []
    idx = 0
    result = [0,0]
    check = words[0][0]
    for i,w in enumerate(words):
        who = (i+1)%n if (i+1)%n !=0 else n
        if done.count(w)>0 or w[0] != check:
            result[0] = who
            result[1] = (i+1)//n+1 if (i+1)%n != 0 else (i+1)//n 
            break
        done.append(w)
        check = w[-1]
    return result
            
        