from collections import Counter
def solution(topping):
    left = Counter(topping)
    left_cnt = len(left)
    right = Counter()
    right_cnt = 0
    result = 0
    for t in topping:
        left[t] -= 1
        if left[t] == 0 :
            left_cnt -= 1
        if t in right:
            right[t] +=1
        else:
            right[t] = 1
            right_cnt +=1
        if left_cnt == right_cnt :
            result +=1
    return result
            
        
        