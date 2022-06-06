def check_prime(num):
	for i in range(2,num):
		if num%i==0:
			return ("Not Prime")
	return ("Prime")

ans = check_prime(14)
print(ans)

message1 = "Global Variable"
def myFunction():
	print("\nINSIDE THE FUNCTION") #Global variables are accessible inside a function 
	print (message1)  #Declaring a local variable 
	message2 = "Local Variable"
	print (message2)

print("\nOUTSIDE THE FUNCTION")
#Global variables are accessible outside function
print (message1)
#Local variables are NOT accessible outside function.
print (message2)
