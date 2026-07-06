n = int(input())

A = set(map(int, input().split()))

m = int(input())

for i in range(m):
    operation, size = input().split()

    B = set(map(int, input().split()))

    if operation == "intersection_update":
        A.intersection_update(B)

    elif operation == "update":
        A.update(B)

    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(B)

    elif operation == "difference_update":
        A.difference_update(B)

print(sum(A))