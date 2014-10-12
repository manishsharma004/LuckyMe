from random import randint
from math import pow

# User input handler
def get_input():
	try:
		raw_input
	except NameError:
		return input()
	else:
		return raw_input()


def main():
	# Ask for luck index(How lucky you feel today)
	print("Please set you luck index: (1 or 2 or 3 or 4)")
	n = get_input()
	n = int(n)

	# Check input validity
	while(not(n==0 or n==1 or n==2 or n==3 or n==4)):
		print("Not a valid luck index, Please enter (1 or 2 or 3 or 4)")
		n = get_input()
		n = int(n)

	# Set n according to luck index given by user
	n = int(pow(10, n))

	# Show chances of the winning
	# Calculated as 1 - (chances of loosing)

	if(n==1):
		print ("Are you really that hopeless??\n")
		n = 2

	print ("You have %f probabilty to win. So, let try your luck." % (1- pow((float(n-1)/n), 4)))

	# 'choice' decides Till when the following loop will run(depends on users choice to play again)
	a = True
	while a:
		# initialize the list
		l = []
		for x in range(0, 4):
			# Generate four random numbers based on user input
			l.append(randint(0, n-1))

		# Ask for an input
		print ("Input a integer(0 to %d): " % (n-1))
		a = get_input()
		a = int(a)

		# Show if the user won or not
		if a in l:
			print("You win!! :-)")	
		else:
			print("You lose :-(")
		# Show user the list for transparency
		print (l)

		# Ask for playing again...
		print("Wanna try again??, Enter y to try your luck again, else anything... ")
		
		a = get_input()
		while(a==''):
			print("Enter 'y' or some other key to proceed...")
			a = get_input()

		if(a=='y' or a=='Y'):
			a = True
		else:
			a = False
		pass

	# Print greetings for playing
	print("Thank you for playing this game :)")


main()
