def getdate():
    import datetime
    return datetime.datetime.now()

def file_writing(client,option):
	with open(client+"_"+option+".txt","a") as f:
		print("Enter the items you had today:")
		item1 = input()
		f.write(item1)


print("1)Anand.\n2)Harry.\n3)Rohan.\nEnter the name of client to add content",end=":")
client = input())
print("1)Diet.\n2)Exercise.\nEnter your type",end=":")
option = input()
if client==1:
	if option==1:
		file_writing(client,option)
		print("Enter the food consumed:")
		item2 = input()
		f.write(item2)
		print("Item added in file successfully.")
	else:
		file_writing(client,option)
		print("Enter the execrise performed:")
		item2 = input()
		f.write(item2)
		print("Item added in file successfully.")
elif client==2:
	if option==1:
		file_writing(client,option)
		print("Enter the food consumed:")
	    	item1 = input()
	    	f.write(item1)
#			getdate()
	else:
		with open("harry_exercise.txt","a") as f:
			print("Enter the execrise performed:")
			item2 = input()
			f.write(item2)
#			getdate()
else:
	if option==1:
		with open("rohan_diet.txt","a") as f:
	    		print("Enter the items you had today:")
	    		item1 = input()
	    		f.write(item1)
#			getdate()
	else:
		with open("rohan_exercise.txt","a") as f:
			print("Enter the execrise performed:")
			item2 = input()
			f.write(item2)
#			getdate()

