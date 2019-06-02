from random import randint
from math import pow

# User input handler
def get_input(input_message=''):
    try:
        raw_input
    except NameError:
        return input(input_message)
    else:
        return raw_input(input_message)


def main():
    # Ask for luck index(How lucky you feel today)
    user_preffered_luck_index = get_input("Please set you luck index: (1 or 2 or 3 or 4)\n")

    # Check input validity
    while(not(user_preffered_luck_index in ['0', '1', '2', '3', '4'])):
        user_preffered_luck_index = get_input("Not a valid luck index, Please enter (1 or 2 or 3 or 4)\n")

    user_preffered_luck_index = int(user_preffered_luck_index)

    if(user_preffered_luck_index < 1):
        print ("Are you really that hopeless?? Setting your luck index to minimum i.e., 1\n")
        user_preffered_luck_index = 1

    # Set n according to luck index given by user ()
    luck_index = int(pow(10, user_preffered_luck_index))

    # Show chances of the winning
    # Calculated as 1 - (chances of loosing)

    print ("You have %f probabilty to win. So, let try your luck." % (1 - pow((float(luck_index-1)/luck_index), 4)))

    # 'choice' decides Till when the following loop will run(depends on users choice to play again)
    will_play = True
    while will_play:
        # initialize the list
        random_list = []
        for x in range(0, 4):
            # Generate four random numbers based on user input
            random_list.append(randint(0, luck_index-1))

        # Ask for an input
        print ("Input a integer (0 to %d): " % (luck_index - 1))
        user_input = get_input()
        user_input = int(user_input)

        # Show if the user won or not
        if user_input in random_list:
            print ("You win!! :-)")
        else:
            print ("You lose :-(")

        # Show user the list for transparency
        print ('You had to chose from: %s' % ', '.join(map(str, random_list)))

        # Ask for playing again...
        will_play = get_input("Wanna try again??, Enter y to try your luck again, else anything... \n")

        while(will_play==''):
            will_play = get_input("Enter 'y' or some other key to proceed...\n")

        if(will_play=='y' or will_play=='Y'):
            will_play = True
        else:
            will_play = False
        pass

    # Print greetings for playing
    print ("Thank you for playing this game :)")


main()
