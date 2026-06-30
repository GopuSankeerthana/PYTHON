#creating a list
nums = [10,20,30]

#accesing elements of a list
print("accesing:",nums[1])

#slicing a list
print("slicing:",nums[1:3])

#adding elements to a list
nums.append(40)
nums.insert(2,25)
print("adding elements:",nums)


#removing elements from a list
nums.remove(20)
nums.pop(1)
print("removing elements:",nums)

#searching for an element in a list
print(20 in nums)
print(nums.index(30))
print(nums.count(10))

#sorting a list
nums.sort()
print("sorting:",nums)

#reversing a list
nums.reverse()
print("reversing:",nums)
nums[::-1] # reversing a list using slicing

#joining lists
nums2 = [50,60]
nums3 = nums + nums2
print("joining lists:",nums3)

#repeating lists
nums4 = nums * 2
print("repeating lists:",nums4)

#length of a list
print("length of a list:",len(nums))

#max and min of a list
print("max of a list:",max(nums))
print("min of a list:",min(nums))

#sum of a list
print("sum of a list:",sum(nums))

#iterating through a list
for i in nums:
    print(i)

#list comprehension
n = [1,3,4]
squared_list = [i**2 for i in n]
print("squared list:",squared_list)

#copying a list
nums_copy = nums.copy()
print("copying a list:",nums_copy)
copy_nums = nums[:] #copying a list using slicing

#nested lists
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print("nested list:",nested_list)