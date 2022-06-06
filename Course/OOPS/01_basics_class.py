class Student():
    comp_std_attandence = 75
    pass

harry = Student()
larry = Student()
print(harry,larry)   #these are 2 different objects of class student.

harry.name = "Harry"
harry.std = 12
harry.section = 1
harry.subjects = ["maths","chemistry","Physics","electronics"]

larry.name = "Larry"
larry.std = 11
larry.section = 2
larry.subjects = ["bio","chemistry","Physics","zology"]

print(harry.subjects[0])
print(larry.subjects)

