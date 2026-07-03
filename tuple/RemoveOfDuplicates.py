t = (1,3,2,4,2,1,3,4,5)
for i in t:
    if t.count(i) > 1:
        t = tuple(x for x in t if x != i)
print(t)