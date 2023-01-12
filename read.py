#留言分析程式

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f :
		data.append(line.strip())
		count += 1  # count = count + 1
		if count % 1000 == 0 : # %為求餘數的意思
			print(len(data))


