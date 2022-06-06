def deco1 (who_am_i):
	def exe_now():
		print("Executing now.")
		who_am_i()
		print("Executed.")
	return exe_now

@deco1
def who_am_i():
    print("I am a developer.")

#who_am_i = deco1(who_am_i)    #here is the main step

who_am_i()
	
