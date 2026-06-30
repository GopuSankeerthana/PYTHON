nums = [0,2,1,0,4,3]
res = []
for i in nums:
    if 0 !=i:
        res.append(i)
if len(res) != len(nums):
    for i in range(len(nums)-len(res)):
        res.append(0)
print(res)
    