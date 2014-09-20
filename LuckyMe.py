from random import randint
from math import pow

# Ask for luck index(How lucky you feel today)
print "Please set you luck index, (1 or 2 or 3 or 4),"
n = raw_input()

# Set the according to luck index given by user
n = int(pow(10, int(n)))


# If the user enter 0
if(n==1):
	n=2

# Show chances of the winning
# Calculated as 1 - (chances of loosing)
print "You will %f probabilty to win. So, let try your luck." % (1- pow((float(n-1)/n), 4))

# 'choice' decides Till when the following loop will run(depends on users choice to play again)
a = True
while a:
	# initialize the list
	l = []
	for x in range(0, 4):
		# Generate four random numbers based on user input
		l.append(randint(0, n-1))

	# Ask for an input
	print "Input a integer(0 to %d): " % (n-1)
	a = raw_input()
	a = int(a)

	# Show if the user won or not
	if a in l:
		print "You win!! :-)"	
	else:
		print "You lose :-("
	# Show user the list for transparency
	print l

	# Ask for playing again...
	print "Wanna try again??, y to try your luck again: "
	a = raw_input()
	if(a=="y"):
		a =  True
	else:
		a = False
	pass

# Print greetings for playing
print "Thank you for playing this game :)"
