def binary_search (a,low,high,x):
	if (high >= low):
		mid = (low+high)//2
		if a[mid] == x:
			return mid
		elif a[mid] > x:
			return binary_search(a,low,mid-1,x)
		else:
			return binary_search(a,mid+1,high,x)
	else:
		return -1

a = [10,8,12,90,21,30]
a.sort()
print(a)
x = int(input("Enter the element:"))
res = binary_search(a,0,(len(a)-1),x)
if res != -1:	
	print("Found.")
else:
	print("Not found.")
