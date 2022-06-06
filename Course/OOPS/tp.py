class Employee:
	no_of_leaves = 10
	
	def __init__ (self, name, salary, role):
	    self.name = name
	    self.salary = salary
	    self. role = role
	
	def __repr__(self):
	    return f'name : {self.name}\nsalary : {self.salary}\nrole : {self.role}'




anand= Employee("anand", 1000, "Developer")
print(str(anand))

