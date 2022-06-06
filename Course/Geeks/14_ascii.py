str1 = "AnanD"
new_name =  []
for i in str1:
	if i.isupper():
		new_name.append(i.lower())
	else:
	    	new_name.append(i.upper())
new_name = ''.join()
print(new_name)

