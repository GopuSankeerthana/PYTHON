n = int(input())
a = list(map(int,input().split()))
l = len(a)
sum = 0
for i in range(0,l):
    sum+=a[i]
print(sum) 