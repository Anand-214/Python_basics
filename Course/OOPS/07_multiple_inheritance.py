class Employee:

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

class Player:
	no_of_games = 4
	def __init__(self, name, games):
		self.name = name
		self.games = games
	
	def print_details(self):
		return f"The name is player is {self.name}, He playes games like: {self.games}"
	
	@classmethod
	def change_no_of_games(cls,new_games):
		cls.no_of_games = new_games

class Cool_emp (Employee, Player):
	pass

karan = Cool_emp("Karan",1234,"Opener")
print(karan.role)
Player.change_no_of_games(5)
print(Player.no_of_games)
		
aarav = Player("Aarav",["Cricket","Soft-ball"])
print(aarav.__dict__)
print(aarav.print_details())

