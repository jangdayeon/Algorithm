def solution(survey, choices):
    check1 = {'R':0, 'T':0}
    check2 = {'C':0, 'F':0}
    check3 = {'J':0, 'M':0}
    check4 = {'A':0, 'N':0}
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    for i, s in enumerate(survey):
        no, yes = s[0], s[1]
        if s == 'RT' or s == 'TR':
            if 1<=choices[i]<=3 :
                check1[no] -= score[choices[i]]
            else :
                check1[yes] -= score[choices[i]]
        elif s == 'CF' or s == 'FC':
            if 1<=choices[i]<=3 :
                check2[no] -= score[choices[i]]
            else :
                check2[yes] -= score[choices[i]]
        elif s == 'JM' or s == 'MJ':
            if 1<=choices[i]<=3 :
                check3[no] -= score[choices[i]]
            else :
                check3[yes] -= score[choices[i]]
        elif s == 'AN' or s == 'NA':
            if 1<=choices[i]<=3 :
                check4[no] -= score[choices[i]]
            else :
                check4[yes] -= score[choices[i]]
    result = ""
    result += sorted(check1, key = lambda x:check1[x])[0]
    result += sorted(check2, key = lambda x:check2[x])[0]
    result += sorted(check3, key = lambda x:check3[x])[0]
    result += sorted(check4, key = lambda x:check4[x])[0]
    return result
    