
animals = [ "whale", "shark", "bear", "dove", "lion" ]

print("hi! today we'll learn about some super cute & cool animals :) here are some options! ")
print(", ".join(str(i) for i in animals))
choice = input("choose the animal you want to learn about! ")

if choice.lower() == "whale": 
    print("whales eat phytoplankton! ")
elif choice.lower() == "shark": 
    print("sharks don't have bones! ")
elif choice.lower() == "bear": 
    print("bears usually live up to 25 years! ")
elif choice.lower() == "dove": 
    print("doves are symbols of peace <3 ")
elif choice.lower() == "lion": 
    print("lions are not afraid to hunt during storms. ")
else: 
    print("please pick a valid animal! ")