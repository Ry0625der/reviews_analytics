#留言分析程式

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f :
		data.append(line.strip())
		count += 1  # count = count + 1
		if count % 1000 == 0 : # %為求餘數的意思
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均程度為', sum_len/len(data))
