class A:
	def met(self):
		print("In class A")

class B(A):
	def met(self):
		print("In class B")

class C(A):
	pass
class D(C, B):
	pass
a = A()
b = B()
c = C()
d = D()

d.met()

#this should be avoided as much as possible to get rid of diamond shape problem.
