# this shyt is wild. So in java, the only variable type that doesnt care about being in global is var
# thats why they say dont use var because var can fuck some code up
# well python is similar. you can make a forloop and call the declaration outside the forloop function


for i in range(1,19):
    cheese = i
    
print(cheese)



# recursion limit is 1000 by default
def recurse(limit, number):
    if number == limit:
       return "We lit. The numbers match each other:\n limit: ", limit, "and number: ",number
    else:
        print("###################\nThe limit is still : ",limit, "\nand\nThe number is: ",number)
        return recurse(limit ,number + 1)
        
        
        
        
userNumber = int(input("Enter a number: "))
userLimit = userNumber * 10

print("Your limit is ", userLimit," which is 10 times your number entered ", userNumber)
print (recurse(userLimit, userNumber))