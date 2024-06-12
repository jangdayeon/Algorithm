#짝홀수에 따라 규칙이 있었음. 규칙을 확인하는 것이 중요했다.
#이문제는 감을 못잡겠어서 그냥 답지 확인 함..

def solution(numbers):
    result = []
    for n in numbers:
        a = '0'+bin(n)[2:] #맨 앞에 0이 없는 경우가 있을 수 있으니 0 추가해야 함
        idx = a.rfind('0')
        a = list(a)
        a[idx] = '1'
        if n % 2 == 0:
            result.append(int(''.join(a),2))
        else :
            a[idx+1] = '0'
            result.append(int(''.join(a),2))
    return result