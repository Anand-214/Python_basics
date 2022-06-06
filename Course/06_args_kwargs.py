def func (normal, *args, **kwargs):
	print(normal)
	print("\n")

	for items in args:
		print(items,end=" ")
	
	for keys,values in kwargs.items():
		print(f"\nName: {keys}, Role: {values}")



normal = "Mirafra"
my_list = ["Akash","Hareesh","Anand","Warma"]
tasks = {"Akash":"Multimedia","Hareesh":"Wifi","Anand":"Video","Warma":"Audio"}
print("Company name:")
print("Employee names are:")
print("The roles given are:")
func(normal, *my_list, **tasks)

