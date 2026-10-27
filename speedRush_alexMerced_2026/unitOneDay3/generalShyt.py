import math

number = 5.78
# you dont need to use math.round() like node.. judt round()
numberRound = round(number)
numberCeiling = math.ceil(number)
numberFloor = math.floor(number)


print(f"##########################\nRounded {number} is {numberRound}. The ceiling of {number} is {numberCeiling}. The floor of {number} is {numberFloor}")
print("############# challenge at 3.14 ################\n for numbers 0 - 10 fins the numbes divisible by 0\n. Remember, for(start, stop AT, count)\n############# challenge at 3.14 ################")
sum = 0
for i in range(0,11,1):
    if i % 2 == 0: # operator . NOT an assignment operator = > < != == += *= %= etc
        sum += i
        print(i, "is divisible by 0\n. end = "" ")
print("The sum of all the even numbers is: ", sum )
    
   
    
    


