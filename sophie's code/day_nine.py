# mathematical program that teaches students about log and exponential expressions

import math
import time

welc = print("hey, welcome to the math program :) today we'll learn how to evaluate log and exponential expressions. ")
time.sleep(3)

# explanations of log vs. exponential
print("an exponential number has a base and an exponent. if an exponential number has a base of 10 and an exponent of 2, the resulting math expression would be 10 times 10 (the number times itself the amount of times the exponent is). ")
time.sleep(3)
print("a log expression is almost the opposite of an exponential expression. we'll learn how to convert log to exponential later in the program, but for now understand that log is the inverse of an exponential function. ")
time.sleep(3)
print("let's learn more about each of these with examples! ")

# allows the user to create an example of their choice
func = input("would you like to use exponents or find the log of a number? ")
num = int(input("what number would you like to work with? " ))
base_exp = int(input("what base / exponent would you like to use? ex: 10. ")) 

def exponential_to_log(num, base_exp): 
    print("as an example, we will use 10^2 = 100. \n when converting this to log, 10 (a) becomes the base, 100 (c) becomes the number we are taking the log of, and 2 (b) ends up being the answer. ")
    time.sleep(3)
    print("let's try this conversion once! ")

    exp = math.pow(num, base_exp)
    print(f"when converting to log, {exp} becomes the answer of log base {base_exp} of {num}. \n the log expression would be written as log subscript {num} of {exp} = {base_exp}. ")

if func.lower() == "exponents" or "exponent":
    ans = math.pow(num, base_exp)
    print(f"{num} to the power of {base_exp} is {ans}. this means {num} was multipled by itself {base_exp} times. ")

    time.sleep(3)
    print("in order to convert an exponential expression to log, understand this: \n EXPONENTIAL FORM: a^b = c \n ex: 10^2 = 100. LOG FORM: log subscript a (this is the base!) of c = b. this will make more sense once we convert the expressions! ")
    time.sleep(3)
    exponential_to_log(num, base_exp)

def log_to_exponential(num, base_exp): 
    print("as an example, we will use log subscript 10 (meaning base 10) of 100. \n what does this equal? in order to make it easier, let's convert it to exponential form. ")
    time.sleep(3)
    print("we'll try this conversion! ")

    log = math.log(num, base_exp)
    print(f"when converting to exponential, the base, in this case {base_exp}, becomes the number we are taking the exponent to. the answer to log base {base_exp} of {num} is easy to see in exponential form. when moving the numbers correctly, the equation becomes 10^x = 100. \n 10 to the power of 2 equals 100, so the log base {base_exp} of {num} = {log}. ")

if func.lower() == "log" or "find log" or "use log":
    ans = math.log(num, base_exp)
    print(f"the log base {base_exp} of {num} is {ans}! ")
    time.sleep(3)
    log_to_exponential(num, base_exp)