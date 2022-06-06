ans = 19
guess = 1
print("Guess game!!!")
print("Guess a number:",end="")

while (guess<=9):
	print("Guess a number:",end="")
	usr_in = int(input())
    	if ans == usr_in:
        	print("You won!!")
        	print(f'You took {guess} chances to win.')
        	break
    	elif (usr_in > ans):
        	print("Guess a lower number.")
        	print("Chances left are",9-guess)
    	else:
        	print("Guess a higher number.")
        	print("Chances left are",9-guess)
    	guess += 1
if guess>9:
    print("Game Over")
