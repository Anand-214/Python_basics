"""d1 = {"Harry":"Burger","Chetan":"Maggie","Shubham":{"B":"Idli","L":"Roti","D":"Rice"}}
print(d1["Shubham"]["D"])
d2 = d1.copy()
del d2["Harry"]
print(d1)
print(d1.values())
print(d1.keys())
"""
my_dict = {"Fear":"Afraid of something","Cheer":"To motivate someone.","Harass":"To trouble someone"}
print("Choose a word from the following:\n1)Fear\n2)Cheer.\n3)Harass.")
print("Enter you choice:",end="")
user_input = input()
print(f'You entered {user_input}')
print("The meaning is:")
print(my_dict[user_input])
