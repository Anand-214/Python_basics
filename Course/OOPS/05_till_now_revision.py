class Library_records:
	issue_per_student = 4
	max_days_issued = 15

	def __init__(self, name, current_year, stream):
		self.name = name
		self.current_year = current_year
		self.stream = stream
	
	@classmethod
	def change_books_limit (cls, new_book_limit):
		cls.issue_per_student = new_book_limit

	@classmethod
	def change_days_alloted (cls, new_days):
		cls.max_days_issued = new_days


anand = Library_records("Anand", "second year", "ENTC")
anand.issue_per_student = 15
print(anand.issue_per_student)
nachiket = Library_records("Nachiket", "first year", "IT")

print(anand.__dict__)
anand.change_books_limit(10)
print(anand.issue_per_student)






























'''class Employee:
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


Employee.print_name("Anand")
Anand = Employee("Anand","$10000", "sr.developer")
print(Anand.__dict__)
Employee.change_leaves(12)
Employee.change_yoj(2020)
#print(Employee.__dict__)
print(Employee.no_of_leaves)
print(Employee.year_of_joining)
'''


