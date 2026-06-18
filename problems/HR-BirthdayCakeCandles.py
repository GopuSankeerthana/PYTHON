n = int(input())
candles = list(map(int, input().split()))
tallest = max(candles)
count = 0
for i in candles:
    if i == tallest:
        count += 1
print(count)