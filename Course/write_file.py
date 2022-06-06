f = open("code.txt","r+")
print(f.read())
f.write("\nLast line.")
f.close()
