def solution(n, wires):
    answer = n #가장 큰 수로 값 초기화
    
    for wire_ab in wires:
        a,b = set(), set()
        a.add(wire_ab[0])
        b.add(wire_ab[1])
        visited = [False] * n
        visited[wire_ab[0]-1],visited[wire_ab[1]-1] = True,True
        while visited != [True]*n :
            for wire in wires:
                if wire_ab == wire :
                    continue
                if wire[0] in a:
                    a.add(wire[1])
                    visited[wire[1]-1] = True
                elif wire[1] in a:
                    a.add(wire[0])
                    visited[wire[0]-1] = True
                elif wire[0] in b:
                    b.add(wire[1])
                    visited[wire[1]-1] = True
                elif wire[1] in b:
                    b.add(wire[0])
                    visited[wire[0]-1] = True
        answer = min(abs(len(b)-len(a)), answer)
    return answer
            