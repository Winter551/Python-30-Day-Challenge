
import random

print("welcome to sophie's manicures :) ")
choice = input("would you like to choose your own set today or randomize one? please pick 'choose' or 'randomize'. ")

colors = [ "white", "brown", "pink", "purple", "blue", "red", "orange", "yellow", "green", "black" ]
styles = [ "french tips", "hearts", "stars" ]

if choice.lower() == "choose":
    color = input("perfect! what color would you like? ")
    style = input("amazing! is there a specific style you'd like? ex: french tips. ")
    print(f"{color} with {style} is such an amazing choice. ")
else:
    color = colors[random.randint(0, 9)]
    style = styles[random.randint(0, 2)]
    print(f"wow, looks like your nails are going to be {color} with {style}! ")