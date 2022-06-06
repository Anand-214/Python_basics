def function1 (a,b):
    """Its a basic print function."""
    print("Hello World!!",a-b)

def function2 (a,b):
    """This function will calculate the average of only two numbers."""
    return (a+b)/2

function1(100,200)
res = function2(10,20)
print (int(res))

print("The doc string for function1 is",end=":")
print(function1.__doc__)
print("The doc string for function2 is",end=":")
print(function2.__doc__)
