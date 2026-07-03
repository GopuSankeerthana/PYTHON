t = (1,3,5,3,2,4,2,1,3,4,5)
count = {}
for i in t:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)   