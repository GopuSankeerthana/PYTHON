n = int(input())
arr = list(map(int, input().split()))

freq = {}

for sock in arr:
    freq[sock] = freq.get(sock, 0) + 1

pairs = 0

for count in freq.values():
    pairs += count // 2

print(pairs)