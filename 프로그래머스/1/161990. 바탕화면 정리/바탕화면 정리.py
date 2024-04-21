def solution(wallpaper):
    minW, maxW, minH, maxH = len(wallpaper[0]),-1,len(wallpaper),-1
    for i, h in enumerate(wallpaper):
        for j, w in enumerate(list(h)):
            if (w=='#'):
                print(i,j)
                minW = min(minW,j)
                maxW = max(maxW,j+1)
                minH = min(minH,i)
                maxH = max(maxH,i+1)
    return [minH,minW,maxH,maxW]