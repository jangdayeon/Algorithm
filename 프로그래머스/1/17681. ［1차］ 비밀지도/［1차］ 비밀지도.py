def solution(n, arr1, arr2):
    # a1 = tenToTwo(n,arr1)
    # a2 = tenToTwo(n,arr2)
    # a3 = map(lambda x,y:int(x)|int(y),a1,a2)
    # print(*a3)
    answer = []
    for i,j in zip(arr1,arr2):
        tmp = str(bin(i|j))[2:]
        tmp = '0'*(n-len(tmp))+tmp
        tmp = tmp.replace('1','#')
        tmp = tmp.replace('0',' ')
        answer.append(tmp)
    return answer

# def tenToTwo(n,arr):
#     arr_2 = ['']*len(arr) #2진수 저장
#     for i,a in enumerate(arr):
#         quotient = a
#         remainder = ''
#         for _ in range(n):
#             quotient = a//2
#             remainder += str(a%2)
#             a = a//2
#         arr_2[i]= remainder[::-1]
#     return arr_2