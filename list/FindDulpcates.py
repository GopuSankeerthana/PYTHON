nums = [2,1,1,3,2,3,1,4,5]

printed = []

for i in nums:
    if nums.count(i) > 1 and i not in printed:
        print(f"{i}: {nums.count(i)}")
        printed.append(i)