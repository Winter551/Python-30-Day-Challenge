#Remainder program

#Asking user for their numbers
num1 = int(input("Pick a number: "))
num2 = int(input("Pick a number you would like to divide your first number by: "))

#Math n stuff
answer = int(num1/ num2)
remainder = int(num1%num2)

#Print stuff
print(f"The answer is {answer}, with a remainder of {remainder}")