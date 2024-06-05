#set함수를 이용해서 len을 비교하면 될 것 같음
#for문은 한 번만
#한 번 틀림. 네.. 시간 초과입니다.
#세 번 틀림. set()함수 만드는 것은 O(N)인 것 같다. 대신 add는 O(1)
#네 번 틀림. 방법을 a: 앞->뒤 b: 뒤->앞으로 해서 개수를 모두 구한 다음 마지막에 a,b를 zip해서 개수가 같은 걸 찾는다!
def solution(topping):
    result = 0
    kinds = len(set(topping))
    a_kinds = [0]
    b_kinds = [0]
    a = set()
    b = set()
    for i in range(len(topping)):
        a.add(topping[i])
        b.add(topping[len(topping)-1-i])
        a_kinds.append(len(a))
        b_kinds.append(len(b))
    b_kinds = b_kinds[::-1]
    for i in range(len(a_kinds)):
        if a_kinds[i] == b_kinds[i]:
            result += 1
    return result