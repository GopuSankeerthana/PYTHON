r = 0
c = 0

for i in range(5):
    row = list(map(int, input().split()))
    
    if 1 in row:
        r = i
        c = row.index(1)
count = 0
while r < 2:
    r += 1
    count += 1
while r > 2:
    r -= 1
    count += 1
while c < 2:
    c += 1
    count += 1
while c > 2:
    c -= 1
    count += 1
print(count)