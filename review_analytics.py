# Read file
# File review and analysis

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1 

		if count % 1000 == 0: # '%' is remainder operation.
			print(len(data))

print('File read complete, total have', len(data), 'datas')

# Calculate average data length
length = 0
for d in data:
	length = length + len(d) # length += len(d)
	
print('Average length of each is', length/len(data))

# Filter if data length < 100
new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('Total have', len(new), 'data length below 100.')

# Filter if data contain 'Good' word.
good = []
for d in data:
	if 'good' in d:
		good.append(d)

print('Total have', len(good), 'data with "good".')