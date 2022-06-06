class Employee:
	no_of_leaves = 10
	year_of_joining =2019

	def __init__(self, name, salary, role):
		self.name = name
		self.salary = salary
		self.role = role
	@classmethod
	def change_leaves(cls, new_leaves):
	    cls.no_of_leaves = new_leaves
	
	@classmethod
	def change_yoj(cls, actual_yoj):
	    cls.year_of_joining = actual_yoj
	
	@staticmethod
	def print_name(str1):
	    print("The employee name is " + str1)

class Programmer(Employee):
	def __init__(self, name, salary, role, languages):
		self.name = name
		self.salary = salary
		self.role = role
		self.languages = languages
	

	def print_lines(self):		
		return f"The programmers name is {self.name}, salary is {self.salary},role is {self.role} and languages known are {self.languages}"

karan = Programmer("Karan", 234, "Validation", ["Python","cpp","Shell Scripting"])
print(karan.print_lines())
print(karan.print_name("Karan_Arjun"))


'''
Employee.print_name("Anand")
Anand = Employee("Anand","$10000", "sr.developer")
print(Anand.__dict__)
Employee.change_leaves(12)
Employee.change_yoj(2020)
#print(Employee.__dict__)
print(Employee.no_of_leaves)
print(Employee.year_of_joining)
'''


