count = 0
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 10000 == 0:
            print(count)
print('total is: ', len(data), 'data')


sum_len = 0
for d in data:
    sum_len += len(d)
print(sum_len / count)


new = []
for d in data:
    if len(d) > 100:
        new.append(d)
print('there are: ', len(new), 'more than 100')



