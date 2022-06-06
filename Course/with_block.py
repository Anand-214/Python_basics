with open("code.txt") as f:
    print(f.readlines())
    print(f.tell())
    print(f.readline())
    print(f.tell())

f = open("code.txt")
print(f.read())
print(f.tell())
f.close()
