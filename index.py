import random
playing = True
number = str(random.randint(10,15))
print("I will generate a number from 10 to 15,and you have to guess it")
print("The game will end when you will guess a number correctly!")
while playing:
    guess = input("What's your guess! \n")
  
    if number == guess:
        print("You have guessed it correctly!!",number)
        print("\nYou won the game")
        break
    
    
    else:
        print("Your guess is wrong , Please try again!! \n")