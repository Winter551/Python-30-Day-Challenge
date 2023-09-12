print("welcome to the remainder program. ")
num = int(input("pick an integer: "))
num2 = int(input("pick an integer you would like to divide your original number by: "))

ans = int(num / num2)
rem = num%num2 

print(f"the answer is {ans} with a remainder of {rem}.")