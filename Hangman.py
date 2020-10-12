#importing the time module
import time
import random
#welcoming the user
name = input("\nHello dear, What is your name? ")

print (f"Hello, {name}! so lets the play hangman game")
time.sleep(1) #wait for 1 second
print (f"Hint: the words are from the animal kingdom\n")
time.sleep(1)
print (f"Start guessing...")
time.sleep(1)


words = ['purcupine', 'antelope', 'giraffe', 'rihnos', 'koala']
# Choosing a random word from the list
word = random.choice(words) #user_guess will be searched here

#word = "elephant" #here we set the secret
guesses = '' #creates an variable with an empty value
#turns = 10 #determine the number of turns
turns = len(word)-3
while turns > 0:  #check if the turns are more than zero
    failed = 0 # make a counter that starts with zero
    for char in word:# for every character in secret_word
        if char in guesses:# see if the character is in the players guess
            print (f"{char}")
        else:
            print ("_")   # if not found, print a dash
            failed += 1  # and increase the failed counter with one
    if failed == 0: # if failed is equal to zero # print You Won
        print ("You won")
        break    # exit the script
  #  print
    guess = input("guess a character:")  # ask the user go guess a character
    guesses += guess    # set the players guess to guesses
    if guess not in word: # if the guess is not found in the secret word
        turns -= 1  # turns counter decreases with 1 (now 9)
        print ("Wrong")   # print wrong  
        print (f"You have {turns} more guesses")# how many turns are left
        if turns == 0:   # if the turns are equal to zero
            print (f"You Lose! the right word is '{word}'")