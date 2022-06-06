z = 100
class Student_info():
	q = 10
	w = 20
	def __init__(self,name,number):
		self.name = name
		self.number = number
		print(f"The name is {self.name} and id is {self.number}")
	
	def new_name(self, new_name):
		self.name = new_name
		print(f"The changed name is {new_name}")
	def add(self,x,y):
		print("Local Variables addition:",x+y)
		print("Class variables multiplication:",self.q*self.w)
		print("Global variable as it is ",z)
	
kid = Student_info("Anand",4096)
kid.new_name("mirafra")
kid.add(10,20)
a = [10,]
b = [20]
print(sum(a,b))
