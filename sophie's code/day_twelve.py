# band member evaluation

print("thanks for interviewing with us today! ")
info = input("do you play an instrument? ")
if info.lower() == "yes": 
    print("you are currently being considered as a potential band member! ")
else: 
    print("sorry, you are underqualified! please check back for other potential jobs :) ")

inst = input("what instrument do you play? ")
print(f"omg i used to play the {inst} when i was younger, too! ")
exp = input("how many years of work experience do you have? ")

if exp > 3: 
    print("you are hired !! practice starts next sunday! ")
else: 
    print("i'm sorry, someone else has taken your spot. please check back with us for other potential jobs! ")