# stats-related class average program
# program discusses how a graph of a class' average test scores looks like

count = 0
total = 0

for i in range(1,8): 
    count = count + 1
    score = int(input("what score did you or a classmate get on the test? the max possible score is 100. "))

    total = total + score
    avg = int(total / count)

    print(f"the class average on this test was {avg}. ")

    if i == 8: 
        break

if avg >= 60 <= 100: 
     print("the data of the class average is skewed left, meaning more people scored higher. ")
elif avg >= 45 <= 60: 
     print("the data of the class average is distributed normally, meaning there is a general bell curve in the average score. ")
else: 
     print("the data of the class average is skewed right, meaning more people scored lower. ")