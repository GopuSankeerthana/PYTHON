age = [20 , 23 , 25 , 30 , 35]
reversed_list = age[::-1]
print(reversed_list)

#without slicing
reversed_list = []
for i in range(len(age)-1,-1,-1): 
    '''stop as -1 includes the first element and step as -1 to go in reverse order'''
    reversed_list.append(age[i])
print(reversed_list)