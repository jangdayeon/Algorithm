def solution(board, moves):
    stack = [] #바구니
    result = 0
    for m in moves:
        for b in board:
            if b[m-1] > 0 :
                if len(stack) > 0 :
                    if stack[-1] == b[m-1] :
                        stack.pop()
                        result +=2
                    else:
                        stack.append(b[m-1])
                else:
                    stack.append(b[m-1])
                b[m-1] = 0
                break
    return result