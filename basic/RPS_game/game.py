from random import randrange

options = ["r", "p", "s"]

def computers_choice():
    return options[randrange(3)]

def evaluate_game(computer, user):
    message = 'You lose'
    if user == 'r':
        print "You choose rock"
    elif user == 'p':
        print "You choose paper"
    elif user == 's':
        print "You choose Scissors"
    if computer == 'r':
        print "Computer choose rock"
    elif computer == 'p':
        print "Computer choose paper"
    elif computer == 's':
        print "Computer choose scissors"
    if computer == user:
        message = "Draw"
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        message = "You won!!"
    elif not (user == 'r' or user == 'p' or user == 's'):
        message = "Input was not valid"
    print message+"\n"

if __name__ == "__main__":
    message = "Input: r for Rock, p for Paper, s for Scissors, e for Exit: "
    choice = raw_input(message)
    while choice != 'e':
        evaluate_game(computers_choice(), choice)
        choice = raw_input(message)