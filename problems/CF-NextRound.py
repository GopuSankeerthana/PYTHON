s , k = list(map(int, input().split()))
scores = list(map(int, input().split()))
count = 0
for i in range(s):
    if scores[i]>=scores[k] and scores[i]>0:
        count+=1
print(count)
