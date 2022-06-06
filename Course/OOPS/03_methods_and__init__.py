class Empolyee():
	def __init__(self,name, salary, role):
		self.name = name
		self.salary = salary
		self.role = role

harry = Empolyee("Harry", 100, "Developer")
print(harry.name)
print(harry.salary)
print(harry.role)
