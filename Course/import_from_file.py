print("Lets import a function and variable from other file.")
print("\n")
print("Imported file2.py")
import file2
print("Its a variable:",file2.a)

file2.foo("Its me")

print("Imported code.py")
import code
print("The addition is:",code.add(10, 20))
x = 10
print(f"The square of {x} is",code.square(x))

print("And the name is:",__name__)
