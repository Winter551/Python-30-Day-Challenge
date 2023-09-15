# guess the word game! 

import random
words = [ "it", "is", "in", "my", "pi" ] 

print("hi! in this game, you'll attempt to guess the second letter of a word based on the first letter! ")
index = random.randint(0, 4)
word = words[index]
first = word[0]

print("the first letter of your word is " + first + "." )
sec_guess = input("make a guess for the second letter of your word! ")

second = word[1]

for i in range(1, 5):
    if sec_guess == second: 
        print("congrats, you got it right! ")
        break
    
    if sec_guess != second: 
        print("sorry, try again! ")
        sec_guess = input("make a guess for the second letter of your word! ")

    if i == 5: 
        print("sorry, you have run out of guesses. come play agian next time! ")
        break