print("Lets capture the time:")
import time
k = 0
while k<50:
    print("k",end="")
    k+=1
	
initial1 = time.time()
print(initial1)
print(f'The actual time taken by while loop:',initial1)
for i in range(50):
	print("f",end="")

time.sleep(10)
initial = time.time()
print(initial)
print(initial - initial1)

