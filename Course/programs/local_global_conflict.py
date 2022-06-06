message1 = "Global Variable"   # (shares same name as a local variable)
def myFunction():
	message1 = "Local Variable" #(shares same name as a global variable)"
	print("\nINSIDE THE FUNCTION")
	print(message1)
# Calling the function 
myFunction()
# Printing message1 OUTSIDE the function 
print("\nOUTSIDE THE FUNCTION")
print (message1)
