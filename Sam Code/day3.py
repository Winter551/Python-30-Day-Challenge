import random


print("This program will randomly select a number from 1-10 and multiply it by your chosen number")
user_num = int(input("Please select your number: "))

rand_num = random.randint(1,10)
sum_num = (user_num * rand_num)

print(f"The random number was: [{rand_num}]")
print(f"The sum of [{rand_num}] and [{user_num}] is [{sum_num}]")