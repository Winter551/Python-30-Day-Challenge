#Ask for table number and people number
print("You are planning for an event in an event hall")
table_num = input("Please select the amount of tables: ")
people_num = input("Please select the amount of people attending the event: ")

#Divide the amount of people by the amount of tables
#Inting it rounds it down, so add 1
num_ppl_table = int((int(people_num) / int(table_num)) + 1)

#Printing user stuff and the math :)
print(f"The amount of people that will be at one table is: {num_ppl_table}")
