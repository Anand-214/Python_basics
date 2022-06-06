print("Enter your age:",end="")
age = int(input())
if age >= 7 and age <= 100:
	if age > 18:
    		print("You can drive.\nLets go on a drive.")
	elif age < 18:
    		print("Not eligible to drive.")
	else:
    		print("Take a driving test first.")
else:
    print("Not a legal age entered.")
