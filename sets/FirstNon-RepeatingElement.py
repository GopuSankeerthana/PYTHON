a = [4,5,1,2,1,4,5]
freq = {}
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for num in a:
    if freq[num] == 1:
        print(num)
        break   