# basic math program that performs a math function based on user input

num = (input("enter a number: "))

if num.isdigit(): 
    print("perfect!")
else: 
    print("please enter a valid number. [ ex: 10 ]. ")

num2 = int(input("enter a second number: "))
func = input("would you like to add, subtract, multiply, or divide? ")

if func.lower() == "add":
    print(int(num) + int(num2))
elif func.lower() == "subtract":
    print(int(num) - int(num2))
elif func.lower() == "multiply": 
    print(int(num) * int(num2))
elif func.lower() == "divide":
    print(int(num) / int(num2))
else: 
    print("please enter a valid math function. [ ex: divide ]")