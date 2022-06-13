import random
print("Rock Paper Scissors \n"
"choose R for rock \n"
"choose P for paper \n"
"choose S for scissors \n")
while True:
    options=["R", "S", "P"]
    cpu = random.choice(options)
    player = None

    while player not in options:

        player=input("what do you pick: ")
        if player not in options:
            print("Error 404, try again")
        else:
            print("You:",player)
            print("CPU:",cpu)
        if player == cpu:
            print("Ït's a tie")
            continue
        elif player == "R":
            if cpu == "S":
                print("Rock beats scissors,You win!")
            if cpu == "P":
                print("Paper beats rock, You lost to computer.")
        elif player == "S":
            if cpu == "P":
                print("Scissors beats Paper, You win!")
            if cpu == "R":
                print("Rock beats scissors, You lost to computer.")
        elif player == "P":
            if cpu == "R":
                print("Paper beats Rock, You win!")
            if cpu == "S":
                print("Scissors beats Paper, You lost to computer.")
        
        exit = input("\nWould you like to play again? Y/N")
        if exit=="N":
            break

            
            