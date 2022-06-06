def my_func (**kwargs):
	if 'fruit' in kwargs:
		print(f"My favourite fruit is {kwargs['fruit']} and veggie is {kwargs['veggie']}")
	else:
		print("No fav found.")
	
	print(kwargs)



my_func(fruit = "apple", veggie = "lettuce")
