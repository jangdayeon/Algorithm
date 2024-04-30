def solution(a, b):
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"] #1/1이 금요일이니깐 금요일부터 시작
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31] #0월,1월,2월...날짜 수
    return day[(sum(days[:a])+(b-1))%7] #1월 1일부터의 날짜수%7
    