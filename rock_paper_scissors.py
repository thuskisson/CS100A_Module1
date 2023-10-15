import random

#Introduction to user
name = input("Hello, what is your name? ")
print((f"Hello {name}, lets play Rock, Paper, Scissors. "))


#Best of 7 loop
cpu_wins = 0
user_wins = 0

while cpu_wins < 4 and user_wins < 4:

    #Ask user for their "throw" or choice.
    throw = int(input("Press 1 for 'rock', 2 for 'paper' and 3 for 'scissors'. "))

    #Tell the user what their choice was
    if throw == 1:
        print("You chose Rock ")
    if throw == 2:
        print("You chose Paper ")
    if throw == 3:
        print("You chose Scissors ")

    #Random number generator
    my_throw = random.randint(1,3)

    #Tell the user what my choice was
    if my_throw == 1:
        print("I chose Rock ")
    if my_throw == 2:
        print("I chose Paper ")
    if my_throw == 3:
        print("I chose Scissors ")

    if throw == my_throw:
        print("It's a tie! ")
        tie = True

    if throw == 1 and my_throw == 2:
        print("My paper beats your rock. ")
        tie = False
        cpu_wins +=1
    if throw == 2 and my_throw == 1:
        print("Your paper beats my rock. ")
        tie = False
        user_wins +=1
    if throw == 2 and my_throw == 3:
        print("My scissors beat your paper ")
        tie = False
        cpu_wins +=1
    if throw == 3 and my_throw == 2:
        print("Your scissors beats my paper ")
        tie = False
        user_wins +=1
    if throw == 1 and my_throw == 3:
        print("Your rock beats my scissors ")
        tie = False
        user_wins +=1
    if throw == 3 and my_throw == 1:
        print("My rock beats your scissors ")
        tie = False
        cpu_wins +=1

    if user_wins >= 4:
        print("Congratulations! You win this series!")
    else:
        print("I win this series. Better luck next time!")