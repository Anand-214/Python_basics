class A:
	classvar1 = "I am class A's class variable"
	
	def __init__(self):
		self.var1 = "I am class A's instance variable."
		self.classvar1 = "Inside class A's constructor."

class B(A):
	classvar2 = "I am class B's class variable"
	
	def __init__(self):
		pass
a = A()
b = B()
print(B.var1)


