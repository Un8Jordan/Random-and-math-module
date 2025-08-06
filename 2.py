import random
options = ["Rock","Paper","Scissors"]

user_choice = input("Choose Rock , Paper , Scissors:  ")
computer_choice = random.choice(options)
print("You Choosed!: ", user_choice)
print("Compuer Choosed!: ", computer_choice)

if user_choice == computer_choice:
    print("It's a Tie!!")

elif user_choice == "rock" and computer_choice == "Scissors":
     print("Rock smashed the scissor!!, You win!")

elif user_choice == "rock" and computer_choice == "Scissors":
     print("Rock smashed the scissor!!, You win!")     

elif user_choice == "paper" and computer_choice == "Rock":
     print("Paper covered the rock!!, You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":
     print("Scissors cut the paper!!, You win!")
else:
     print("You lose!!, Better luck next time!")