nums = list(map(int,list(input())))
changeWhat = [0,0]
now = nums[0]
changeWhat[now]+=1
for i in range(1,len(nums)):
    if(now != nums[i]):
        now = nums[i]
        changeWhat[now]+=1
print(min(changeWhat))  