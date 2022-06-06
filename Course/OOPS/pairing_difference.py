list_1 = [8,10,7,3,5]
n = int(input("Enter the difference:"))
for i in range(len(list_1)):
	for j in range(len(list_1)):
		if list_1[j] - list_1[i] == n:
		    print(f"Pair found {list_1[i]} and {list_1[j]}")

