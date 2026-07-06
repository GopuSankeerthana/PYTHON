a = [1,2,3,2,3,2,3,2,4,3,2,3,]
freq = {}
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(min(freq, key=freq.get)) #dont compare keys , compare values of the keys