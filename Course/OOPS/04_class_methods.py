class Employee():
	no_of_leaves = 10
	year_of_joining = 2020

	def __init__(self, name, salary, role):
		self.name = name
		self.salary = salary
		self.role = role
	
	@classmethod
	def change_leaves_and_YOJ(cls, new_leaves, new_yoj):
	    cls.no_of_leaves = new_leaves
	    cls.year_of_joining = new_yoj
	
	@staticmethod
	def print_string(str1):
	    print("This is a string " + str1) 


harry = Employee("Harry",123, "Developer")
harry.no_of_leaves = 20
print(harry.no_of_leaves)
'''print(harry.__dict__)
Employee.change_leaves_and_YOJ(15, 2021)
print(Employee.no_of_leaves)
print(harry.year_of_joining)
harry.print_string("Harry")
	
print(type(list))'''
