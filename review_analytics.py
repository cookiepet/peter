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

print(data[0])

# Word count function.

wc = {} # word_count
# Nested for loop
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # Add new key in dictionary.

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('Please input the word you want to search:')
	if word == 'q':
		break
	if word in wc:
		print('Total have', word, ':', wc[word])
	else:
		print('The', word, 'is not included in dictionary.')

print('Thank you.')

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

# Quick method (list comprehension)
# good = [d for d in data if 'good' in d]
# Output = [[number-1] for number in reference if condition]
# output: Result array
# [number-1]: Target object to be putted into array
# number: Filter target.
# reference: Target array which need to be screened

bad = ['bad' in d for d in data]
print(bad)

# 'Bad' in d true and false result will be added into bad array