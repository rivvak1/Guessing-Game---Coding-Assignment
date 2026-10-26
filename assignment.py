import random

# recently i learnd that when making values u dont have to use _, and can capitalise 
# letters instead
randNum = random.randint(1,10)
#random is our imported thingy
# randint meands random integer, so we are making randNum be a random int between 1-10
previGuess = []
# the brackets are a list, this setup is similar to having num = 0, where our list
# is empty

corrAnsw = False
# i learned that a while loop is basically the exact same thing as an if statement, 
# only that a while loop repeats

while not corrAnsw:
    userGuess = int(input("Enter a number between 1 and 10: "))
#the thing above makes it so while answer isnt correct it makes sure to ask you again

    while userGuess < 1 or userGuess > 10 or userGuess in previGuess:
        if userGuess < 1 or userGuess > 10:
            print("Invalid input! - number outside of range.")
            userGuess = int(input("Pick a number between 1 and 10:"))
        else:
            print("invalid input! - number already guessed.")
            userGuess = int(input("Pick a number between 1 and 10:"))

# what i did above is i made a while loop which acts like a fence around the if statement
# then if the number passes thru the while loop, means theres something wrong,
# the if statement finds whats wrong
# aka while loop checks IF theres and issue, if checks WHATS the issue.

    previGuess.append(userGuess)
# this makes it so userguess is then stores into previguess

    if userGuess == randNum:
        print("You guessed correctly!, the number was", randNum)
        print("Your guesses:", previGuess)
        corrAnsw = True
    elif userGuess > randNum:
        print("Try again! The random number is lower!")
        print("Your guesses:", previGuess)
    else:
        print("Try again! The random number is higher!")
        print("Your guesses:", previGuess)