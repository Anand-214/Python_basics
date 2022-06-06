a  =  [2, 5, 7, 8] 
b  =  [3, 4, 9]
#if b[j] > a[i] add b[j] to a
for i in range(len(a)):
	for j in range(len(b)):
		if b[j] > a[i]:
			b.insert((i+1),b[j])
print(a)
