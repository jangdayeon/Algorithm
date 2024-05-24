# 한 번 틀림. 다 런타임 에러 발생 -> 리스트 범위를 넘어가는 문제

def solution(arr1, arr2):
    arr2_2 = [[0] * len(arr2) for _ in range(len(arr2[0]))] #둘 다 곱하기 쓰면 주소 복사되어서 문제생김
    #어제 본 건 같은 주소를 써도 값이 변하면 주소가 변한다고 했는데, 이건 왜 안되는지 모르겠음
    result =[[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for j in range(len(arr2[0])):
        for i in range(len(arr2)):
            arr2_2[j][i] = arr2[i][j]
    
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = sum(map(lambda x,y:x*y, arr1[i], arr2_2[j]))
    return result
    