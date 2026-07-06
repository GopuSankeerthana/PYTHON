n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = set(map(int, input().split()))

result = sorted(A ^ B)

for i in result:
    print(i)