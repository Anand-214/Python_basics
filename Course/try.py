my_dict = {"Fear":"Something","Fear":"Afraid of something","Cheer":"To motivate someone.","Harass":"To trouble someone","Empty":""}

#print(my_dict.keys())
#print(my_dict.values())
#print(my_dict.items())
my_dict.pop("Empty")
print(my_dict)
my_dict.fromkeys("Fear")
#my_dict.update("Empty":"Nothing")
print(my_dict)


my_list = [5,]
new_list = [x*x for x in my_list]
print(new_list)

t = (1,2,3)
t = (4,5,6)
print(t)
