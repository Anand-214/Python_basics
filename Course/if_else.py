print("Enter first number:",end="")
var1 = int(input())
print("Enter second number:",end="")
var2 = int(input())
if var1>var2:
    print(f'{var1} is greater than {var2}')
elif var1<var2:
    print(f'{var1} is lesser than {var2}')
else:
    print("These two numbers are same.")

