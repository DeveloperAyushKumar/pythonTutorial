i=0
while(i<20):
    print(i)
    i+=1

nums=[2,4,5,66,4,9]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1
    if(idx==5):
        break

for el in nums:
    print(el)

for el in nums:
    if(el==7):
        print("7 found")
        break
    print(el)
else :
    print("only execute when loop has complety executed without hitting break")
# range(start,stop,step)
for i in range(5):
    print(i)
# print(range(6))


    


