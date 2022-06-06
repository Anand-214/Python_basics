class Employee():
    no_of_leaves = 10
    pass

print(Employee.no_of_leaves)
Employee.no_of_leaves = 15
print(Employee.no_of_leaves)


harry = Employee()
larry = Employee()

harry.id = 1223
harry.role = "Trainer"


larry.id = 1223
larry.role = "Trainer"
print(larry.__dict__)
larry.no_of_leaves = 12
print(larry.__dict__)

