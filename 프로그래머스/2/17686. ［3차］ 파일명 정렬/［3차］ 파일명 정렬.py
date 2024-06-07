def solution(files):
    new_files = []
    # new_files = [['img', '12', '.png'], ['img', '10', '.png']] ##################
    for f in files:
        start = 0
        end = 0
        for j,ff in enumerate(f):
            if start > 0 and end > 0 and not ff.isnumeric():
                break
            if ff.isnumeric() and start == 0:
                start = j
                end = j+1
            elif ff.isnumeric():
                end = j+1
        new_files.append([f[:start],f[start:end],f[end:]]) 
    ################################################################################
    new_files.sort(key = (lambda x: ( x[0].lower(),int(x[1]) ))) #Head 기준 사전 순 정렬
    result = []
    for n in new_files:
        result.append("".join(n))
    return result
            