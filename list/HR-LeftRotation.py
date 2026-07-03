n, d = map(int, input().split())
arr = list(map(int, input().split()))

print(*arr[d:] + arr[:d])