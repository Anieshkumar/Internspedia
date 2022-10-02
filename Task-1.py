import random
import math
A = int(input("Enter lower bound:- "))
B = int(input("Enter upper bound:- "))
x = random.randint(A, B)
print("\n\tYou've only ",
	round(math.log(B - A + 1, 2)),
	" chances to guess the integer!\n")


count = 0


while count < math.log(B - A + 1, 2):
	count += 1

	
	guess = int(input("Guess a number:- "))

	
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")


if count >= math.log(B - A + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")


