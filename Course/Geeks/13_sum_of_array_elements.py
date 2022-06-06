#--------------------Sum of array elements------------------#
'''array = [10, 15, 18, 20]
sum = 0
for x in array:
	sum += x	
print(sum)
'''
#---------------To check number prime or not.-----------------#
'''
num = int(input("Enter the number to check its prime or not:"))
flag = 0
for i in range(2,num):
	if num%i == 0:
		flag = 1
		break
	else:
		flag = 0

if flag == 0:
	print("Prime")
else:
	print("Not a prime.")
'''
#------------------------Largest of the array--------------------------#
'''array = [10, 15, 58, 200]
largest = 0
for i in array:
	if i > largest:
		largest = i

print("The largest is {}".format(largest))
'''
#-------------Square of first n natural numbers-----------------------#
'''num = int(input("Enter the number upto which need square:"))
for i in range(1,num+1):
    print("{}\t:\t{}".format(i, i**2))
'''
#-------------Cube of first n natural numbers-----------------------#
'''num = int(input("Enter the number upto which need cube:"))
for i in range(1,num+1):
    print("{}\t:\t{}".format(i, i**3))
'''
#-------------sum of square of first n natural numbers-----------------------#
'''num = int(input("Enter the number upto which need sum of square:"))
sum = 0
for i in range(1,num+1):
	sum += (i**2)
print(sum)

'''
#-------------sum of cube of first n natural numbers-----------------------#
'''num = int(input("Enter the number upto which need sum of cube:"))
sum = 0
for i in range(1,num+1):
	sum += (i**3)
print(sum)
'''
#------------- ASCII value of character-----------------------#
'''c = 'Z'
print(ord(c))
'''
print (chr(67))

