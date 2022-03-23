count = 0
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 10000 == 0:
            print(count)

print(data[2])
