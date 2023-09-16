# class rank in percentiles

gpa = float(input("what is your unweighted gpa on a 4.0 scale? "))
grade = int(input("what did you get on your last math test? "))

if gpa >= 3.8 and grade >= 80: 
    print("you are likely in the 90th percentile or higher in your class! ")
elif gpa >= 3.5 and grade >= 70: 
    print("you are likely in the 50th percentile or higher of your class. ")
else: 
    print("you are likely lower than the 50th percentile of your class. u can do it! ")