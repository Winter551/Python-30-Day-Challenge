#Rounding to the user-selected decimal place

user_float = float(input("Please input a float value [Ex. 1.278]: "))
print("Please select the number of decimal places it should round to")
print("[Ex. 1.2345 = [3] 1.235]")
user_max_dec = int(input("> "))

if user_float == int:
  print("This is not a float, please try again")
else:
  print(f"Your float value rounded to the [{user_max_dec}] is: {round(user_float, user_max_dec)}")
