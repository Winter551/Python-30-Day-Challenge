# showcases height in comparison to the average height of men/women in the us

avg_w = 5.4
avg_m = 5.9 

height = float(input("how tall are you? please enter the number with a decimal rather than a comma. [ ex: 5.9 = 5'9 ] "))
gen = input("are you male or female? ") 

if gen.lower() == "male":
    if height >= 5.9: 
        print("you are the average height or taller than the average height of a typical male in the us. ")
    else: 
        print("you are shorter than the average male in the us, which is perfectly okay! ")

if gen.lower() == "female": 
    if height >= 5.4:
        print("you are the average height or taller than the average height of a typical female in the us. ")
    else: 
        print("you are shorter than the average female in the us, which is perfectly okay! ")
