n = int(input())
scores = list(map(int, input().split()))
highest_score = scores[0]
lowest_score = scores[0]
highest_count = 0
lowest_count = 0
for i in range(0,len(scores)):
    if scores[i]>highest_score:
        highest_score = scores[i]
        highest_count += 1
    elif scores[i]<lowest_score:
        lowest_score = scores[i]
        lowest_count += 1
print(highest_count, lowest_count)