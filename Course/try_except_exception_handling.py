print("Enter the first number:",end="")
num1 = input()
print("Enter the second number:",end="")
num2 = input()
try:
    print(f'Addition of {num1} and {num2} is',int(num1)+int(num2))
except Exception as e:
    print(e)

print("This is a important line.")

