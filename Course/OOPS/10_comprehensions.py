#list_1 = [i for i in range(100) if i%7 ==0]
#print(list_1)

#my_dict = {i:f"Item{i}" for i in range(10)}
#print(my_dict)

#new_dict = {key:value for key,value in my_dict.items() if key%2==0}
#print(new_dict)

#list_2 = [i for i in range(10) if i>5]
#print(list_2)

#dict_2 = {value:key for key,value in my_dict.items()}
#print(dict_2)

#dict_2 = {i:i**2 for key,value in }
#print(dict_2)
#dresses = {dress for dress in ["dress1","dress2","dress1","dress2"]}
#print(dresses)
#set_1 = {i for i in range(10) if i>5}
#print(id(set_1))
#print(type(set_1))

#__________________________________________________________________________________________________________________

list_1 = [i for i in range(10) if i%2 == 0]
print(list_1)

list_2 = [i for i in range(10) if i%3 != 0]
print(list_2)

dict_1 = {i:f"Items{i}" for i in range(10)}
print(dict_1)

my_dict = {0:"Item0",1:"Item1",2:"Item2",3:"Item3",4:"Item4"}
print(my_dict)

comp_dict = {value:key for key,value in my_dict.items()}
print(comp_dict)

dresses = {dress for dress in ["dress1","dress2","dress2","dress1","dress2"]}
print(dresses)
print(id(dresses))
print(type(dresses))

(a,b,*c,d) = [1,2,3,4,5,6]
print(c)
