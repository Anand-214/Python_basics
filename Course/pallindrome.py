print("Enter the word to check its pallindrome or not:",end="")
usr_ip = input()
rev = usr_ip[::-1]
if usr_ip == rev:
    print("Its a pallindrome.")
else:
    print("Not.")
