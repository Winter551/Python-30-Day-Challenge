# guessing your fav type of chocolate :) 

import random

choc = [ "white chocolate", "dark chocolate", "milk chocolate", "peppermint chocolate", "raspberry chocolate" ]
print("chocolate is my fav treat, so i'm going to guess your favorite type :) ")

index = random.randint(0, 4)
guess = choc[index] 
index2 = random.randint(0, 4)
guess2 = choc[index2]

for i in range (1, 2): 
    result = input(f"is your favorite type of chocolate {guess}? type 'yes' or 'no'. ")
    if result.lower() == "yes": 
        print("yay! thanks for playing :) ")
    else: 
        print("aww, sorry! here's my last guess: ")
        result = input(f"is your favorite type of chocolate {guess2}? type 'yes' or 'no'. ")