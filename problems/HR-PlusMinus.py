a = list(map(int,input().split()))
len = len(a)
zero = 0
positive = 0
negative = 0
for i in range(len):
    if a[i]==0:
        zero+=1
    elif a[i]>0:
        positive+=1
    else:
        negative+=1
print(f"{positive/len:.6f}")
print(f"{negative/len:.6f}")
print(f"{zero/len:.6f}")
