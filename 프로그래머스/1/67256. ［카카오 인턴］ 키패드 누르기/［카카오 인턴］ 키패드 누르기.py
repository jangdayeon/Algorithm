def solution(numbers, hand):
    result = ""
    dic = [0,0,0,0,0,0,0,0,0]
    dic[2] = {'#':4, '*':4, 0:3, 1:1, 2:0, 3:1, 4:2, 5:1, 6:2, 7:3, 8:2, 9:3}
    dic[5] = {'#':3, '*':3, 0:2, 1:2, 2:1, 3:2, 4:1, 5:0, 6:1, 7:2, 8:1, 9:2}
    dic[8] = {'#':2, '*':2, 0:1, 1:3, 2:2, 3:3, 4:2, 5:1, 6:2, 7:1, 8:0, 9:1}
    dic[0] = {'#':1, '*':1, 0:0, 1:4, 2:3, 3:4, 4:3, 5:2, 6:3, 7:2, 8:1, 9:2}
    
    left = '*'
    right = '#'
    for n in numbers:
        if n in [1,4,7]:
            result += "L"
            left = n
        elif n in [3,6,9]:
            result += "R"
            right = n
        else:
            if dic[n][left] < dic[n][right] :
                result += "L"
                left = n
            elif dic[n][left] > dic[n][right] :
                result += "R"
                right = n
            else :
                if hand == "left" :
                    result += "L"
                    left = n
                else:
                    result += "R"
                    right = n
    return result
    
    