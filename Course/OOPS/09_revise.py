str1 = "Pam"
x = type(str1.split('a'))
print(x)
print("S"+str1[1:])
my_list = ["10","3","5","12"]
my_list = list(map(int, my_list))
my_list.sort()
print(my_list)
def num_gtr_5(num):
	for i in range(len(my_list)):
		if num > 5:
			return num
new_list = list(filter(num_gtr_5, my_list))
print(new_list)

for i in range(0,9):
	print(i)
'''f = open("qwerty.txt","a+")
f.write("New Line added\nLast line\n")
f.seek(0)
print(f.read())
f.close()

f = open("new.txt","w+")
f.write("New file created\nAdding lines using f.write")
f.seek()
#print(f.read())
f.close()

def getdate():
    import datetime
    print(datetime.datetime.now())

with open("new.txt","a+") as fp:
    fp.write("\nAnand\nKulkarni\nMirafra")
    fp.seek(0)
    print(fp.read())
    getdate()
'''

