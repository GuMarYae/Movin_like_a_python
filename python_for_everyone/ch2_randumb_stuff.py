#python
import random
import math
print("#####################################################")
number = 10;
randomNumber = math.ceil((random.random()));

print(randomNumber);

name = "Tony";
name2= "_Daniels"
age = 39
age_str= str(age)

# only concatinate with numbers or converting ints to strings vice versa
print(name + name2)
# with a string use '+' not ','
print(name + " " + age_str)

print("___________")

#length from 0 index
length = len(name)-1
# I like psuedo coding out loud or in my head 
# i said last is the "last index of name" meaning  i did [last_index] first
# and typed the name variable to the left of it to make sense
# good doing it like this for arrays
last = name[length]
      
print("- From 0 index, length is ", length)
print("- To get the right indexes, length has to start from 0. the last index is ", last)

#using the replace(old,new)
name3 = name.replace("Tony", "Gu")
name4 = name2.replace("Daniels", "Maryae")

print(name3 + name4)
print("--Interesting, notice in name2, I had _Daniels but dint include the '_' for name 4. So it kept the underscore \n If you did want to remove the underscore too, you’d have to include it: \n _Daniels, Maryae ")
################ inuts outputs ######################

#input is not storing "what is your first name", its storing the answer to the question
#then automatically outputs it
first_name = input ("what is your first name");
#important 💥100 percent💥 to always convert a string to a number when not computing
weight = input("How much do you weigh: " );
weight_number = int(weight);

print("your weight is ",weight_number)

#________________________________ Random stuff _______________________________________
PENNIES_PER_DOLLAR = 100
# constant used to convert dollars into pennies

PENNIES_PER_QUARTER = 25
# constant used to calculate quarter change later

#getting the input from the user
userInput = input("Enter the bill value (1 = $1 bill, 5 = $5 bill, etc.): ")
# input always comes in as a string, even if the user types a number

#as soon as you get the input, convert tp. a float, int something
#remember these are always strings of characters when entering inputs
userInputIntBillValue = int(userInput)
# now the bill value is an integer and can be used in math

#since we stored the userInput in as userInputInt, we can freely
#use userInput again
userInput = input("Enter Item price in pennies: ")
# reuse the same variable to save memory and keep code simple

userInputIntItemPrice = int(userInput)
# convert item price from string to integer

changeDue = PENNIES_PER_DOLLAR * userInputIntBillValue - userInputIntItemPrice
# calculate total change due in pennies

dollarCoins = changeDue // PENNIES_PER_DOLLAR
# integer division gives how many whole dollar coins fit into the change





