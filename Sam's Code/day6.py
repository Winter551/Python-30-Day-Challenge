#I have no clue what I want to make this day about so i'll do whatever

#Making variables
var1 = ("This is a variable")
var2 = ("this is also a variable")
var3 = ("this is another variable")

#Basically making a var true will run the loop while once you want it broken you can make it false
running = True

#Picked up this new way of doing while loops from a video, I didn't utilize it correctly, but its still cool
while running:

    user_var = int(input("How many variables do you want in your string? [0-3]: "))

    #Ez if statments and fstrings
    if user_var == 0:
        print("You chose 0 strings :( , try again")
        print()
    elif user_var == 1:
        print(f"{var1}.")
        print()
        break
    elif user_var == 2:
        print(f"{var1}, and {var2}.")
        print()
        break
    elif user_var == 3:
        print(f"{var1}, and {var2}, also {var3}.")
        print()
        break
    else:
        print("This is not a valid number of variables, try again.")
        print()

print("Thanks for choosing variables with me.")

#Adding comments is fun cuz i can look back at my work and understand it better
#Also I like typing fast vroooommmmmmm