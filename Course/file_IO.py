f = open("first_file.txt","w+")
f.write("This is some practice on file handling\n")
f.write("Lets mak it perfect")
f.seek(0)
print(f.readline())
f.close()

