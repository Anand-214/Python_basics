a = [1,2,3,[9,8,7]]
#print(a)
blank = []
var = a[:3]
rev = var[::-1]
print(rev)
for i in range(len(rev)):
	blank.append(rev[i])
print("blank :",blank)
res = a[3][::-1]
blank.insert(0,res)
print(blank)

