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

length = 0
for d in data:
	length = length + len(d) # length += len(d)
	
print('Average length of each is', length/len(data))