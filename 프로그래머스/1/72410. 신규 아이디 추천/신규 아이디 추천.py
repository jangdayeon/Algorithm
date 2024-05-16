def solution(new_id):
    #1단계
    new_id = new_id.lower()

    #2단계
    new_id_tmp = ""
    for n in new_id:
        if n.islower() or n.isdigit() or (n in ["-","_","."]):
            new_id_tmp += n
    new_id = new_id_tmp
    
    #3단계
    new_id_tmp = ""
    dot = False
    for n in new_id:
        if n == ".":
            if dot:
                continue
            else:
                dot = True
        else:
            dot = False
        new_id_tmp += n
    new_id = new_id_tmp

    #4단계
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]
    
    #5단계
    if not new_id:
        new_id = "a"
    
    #6단계
    if len(new_id)>=16 :
        new_id = new_id[:15]
        if new_id and new_id[-1] == ".":
            new_id = new_id[:-1]
        
    #7단계
    if len(new_id)==1 :
        new_id = new_id + new_id[-1]*2
    elif len(new_id)==2 :
        new_id = new_id + new_id[-1]
    
    return new_id