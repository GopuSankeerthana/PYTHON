n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

total_sum = sum(arr)
mysum = 0
count = 0

for i in range(n):
    mysum += arr[i]
    count += 1
    
    if mysum > total_sum - mysum:
        print(count)
        break