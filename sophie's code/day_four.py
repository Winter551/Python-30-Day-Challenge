cookies = 100
amt = int(input(("hi, welcome to the cookie store! how many cookies would u like to order today? note: we only have 100 baked per hour and each cookie is $1. ")))
ppl = int(input("how many people are you sharing your order with? ")) + 1

per = int(amt / ppl)
cost = amt * 1
print(f"awesome! your total is {cost} and each person will get about {per} cookie(s). ")