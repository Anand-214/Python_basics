all_books = ["Wings of fire","Rich Dad Poor Dad","Atomic Habbits"]
class Library:
    #	def __add
	
	@classmethod
	def display(cls):
		for i in range(len(all_books)):
			print (f"{i}){all_books[i]}")
	@classmethod
	def lend(cls, book_name, user):
		cls.book_name = book_name
		cls.user = user
		if cls.book_name in all_books:
			ind = all_books.index(cls.book_name)
			popped = all_books.pop(ind)
			print (f"{popped} lended to {cls.user}")
		else:
			print(f"{cls.book_name} currently not avaibale.")
	
	@classmethod
	def add(cls, add_book, user):
		cls.add_book = add_book
		cls.user = user
		all_books.append(cls.add_book)
		print(f"Stock Updated!!\nCurrent available books : {all_books}")


if __name__ == '__main':
		

print("WELCOME TO THE CENTRAL LIBRARY PORTAL!!")
user = input("Enter your User name : ")
option = "y"
while option == "y":
	print("1)Display Books\n2)Lend Book\n3)Return Book.")
	inp = int(input("Enter your option:"))

	if inp == 1:
		Library.display()
	elif inp == 2:
		print(f"The available books in stock are:")
		for i in range(len(all_books)):
			print(f"{i}){all_books[i]}")
		book_name =str(input("Enter the Book you want to lend:"))
		Library.lend(book_name, user)
	elif inp == 3:
		add_book = input("Enter the Bokk you want to submit:")
		Library.add(add_book, user)
	else:
		print("Please select appropriate option to proceed.")

		
	
	print("Do you want to continue?(y/n):",end="")
	option = input()
	if option != "y":
		break



